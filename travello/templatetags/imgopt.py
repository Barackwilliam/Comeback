"""
Image helpers for faster pages.

    {% load imgopt %}
    <img src="{{ tour.image|ucare:800 }}" loading="lazy" decoding="async">

`ucare` asks Uploadcare for a resized copy in the best format the visitor's
browser supports (WebP/AVIF) instead of the full-size original upload, which
is often a multi-megabyte phone photo. Values that aren't Uploadcare images
(static files, other hosts, empty values) are returned unchanged.
"""
import re

from django import template

register = template.Library()

_UUID = r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
_UCARE = re.compile(
    rf"^(?P<base>https?://[^/]*(?:ucarecdn\.com|ucarecd\.net|ucarecdn\.net)/)?"
    rf"(?P<uuid>{_UUID})(?:/(?P<rest>.*))?$",
    re.IGNORECASE,
)
# Operations we set ourselves, so any already in the stored URL are dropped.
_REPLACED_OPS = {"format", "quality", "progressive", "preview", "resize", "scale_crop"}


@register.filter
def ucare(value, width=800):
    if not value:
        return value
    match = _UCARE.match(str(value).strip())
    if not match:
        return value

    try:
        width = int(width)
    except (TypeError, ValueError):
        width = 800

    # Keep editing operations such as crop/rotate that were applied on upload.
    kept = []
    for op in (match.group("rest") or "").split("/-/"):
        op = op.strip("/")
        if op.startswith("-/"):
            op = op[2:]
        if not op or "/" not in op and "." in op:  # empty, or a trailing filename
            continue
        if op.split("/", 1)[0] in _REPLACED_OPS:
            continue
        kept.append(op)

    base = match.group("base") or "https://ucarecdn.com/"
    ops = "".join(f"-/{op}/" for op in kept)
    return (
        f"{base}{match.group('uuid')}/{ops}"
        f"-/preview/{width}x{width}/-/format/auto/-/quality/smart/"
    )
