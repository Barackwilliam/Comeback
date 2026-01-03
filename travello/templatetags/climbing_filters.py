# travello/templatetags/climbing_filters.py

from django import template

register = template.Library()

@register.filter
def get_dynamic_image(item, num):
    field_name = f"image_{num}"
    return getattr(item, field_name, None)

@register.filter
def get_dynamic_title(item, num):
    field_name = f"title_{num}"
    return getattr(item, field_name, None)
