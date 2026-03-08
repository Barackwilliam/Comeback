"""
JamiiTek Website Status Middleware
====================================
Install this middleware on any Django client website managed by JamiiTek.

INSTALLATION:
1. Add to the client's settings.py:

    JAMIITEK_API_KEY = "your-api-key-from-panel"
    JAMIITEK_API_URL = "https://jamiitek.co.tz/api/site-status/"

    MIDDLEWARE = [
        ...
        'jamiitek_middleware.JamiiTekStatusMiddleware',
    ]

2. Copy this file into the root directory of the client's project
   (same folder as manage.py) and name it `jamiitek_middleware.py`.

NOTES:
- Status is cached for 5 minutes to avoid excessive API calls.
- If the API is unreachable, the site continues working (fail-open).
- Enabled features are accessible via: request.jamiitek_features
"""

import requests
import logging
from django.conf import settings
from django.http import HttpResponse
from django.core.cache import cache

logger = logging.getLogger(__name__)

SUSPENSION_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Service Suspended</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    display:flex; align-items:center; justify-content:center;
    min-height:100vh; background:#f8fafc; font-family:Arial,sans-serif;
  }}
  .container {{
    text-align:center; background:white; padding:60px 50px;
    border-radius:16px; box-shadow:0 4px 30px rgba(0,0,0,0.1);
    max-width:500px; margin:20px;
  }}
  .icon {{ font-size:70px; margin-bottom:20px; }}
  h1 {{ color:#dc2626; margin-bottom:15px; font-size:26px; }}
  p {{ color:#6b7280; line-height:1.7; font-size:15px; }}
  .footer {{ margin-top:35px; color:#d1d5db; font-size:12px; }}
</style>
</head>
<body>
<div class="container">
  <div class="icon">🔒</div>
  <h1>Service Suspended</h1>
  <p>{message}</p>
  <div class="footer">Powered by JamiiTek</div>
</div>
</body>
</html>
"""

MAINTENANCE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Under Maintenance — Back Soon</title>
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{
    display:flex; align-items:center; justify-content:center;
    min-height:100vh; background:#fffbeb; font-family:Arial,sans-serif;
  }}
  .container {{
    text-align:center; background:white; padding:60px 50px;
    border-radius:16px; box-shadow:0 4px 30px rgba(0,0,0,0.08);
    max-width:500px; margin:20px;
  }}
  .icon {{ font-size:70px; margin-bottom:20px; }}
  h1 {{ color:#d97706; margin-bottom:15px; font-size:26px; }}
  p {{ color:#6b7280; line-height:1.7; font-size:15px; }}
  .footer {{ margin-top:35px; color:#d1d5db; font-size:12px; }}
</style>
</head>
<body>
<div class="container">
  <div class="icon">🔧</div>
  <h1>Under Maintenance</h1>
  <p>{message}</p>
  <div class="footer">Powered by JamiiTek</div>
</div>
</body>
</html>
"""


class JamiiTekStatusMiddleware:
    """
    Checks the site's status from the JamiiTek management panel on every
    request and blocks access if the site is suspended or under maintenance.
    """

    CACHE_KEY = 'jamiitek_site_status'
    CACHE_TIMEOUT = 300  # 5 minutes
    BYPASS_PATHS = ['/admin/', '/api/', '/static/', '/media/']

    def __init__(self, get_response):
        self.get_response = get_response
        self.api_key = getattr(settings, 'JAMIITEK_API_KEY', None)
        self.api_url = getattr(
            settings, 'JAMIITEK_API_URL',
            'https://jamiitek.co.tz/api/site-status/'
        )

    def __call__(self, request):
        # Always allow admin, API, static, and media paths through
        for path in self.BYPASS_PATHS:
            if request.path.startswith(path):
                return self.get_response(request)

        # Skip if no API key is configured
        if not self.api_key:
            return self.get_response(request)

        status_data = self._get_status()

        if status_data:
            request.jamiitek_features = status_data.get('features', {})
            request.jamiitek_status = status_data.get('status', 'active')

            site_status = status_data.get('status', 'active')
            message = status_data.get(
                'suspension_message',
                'This service has been suspended. Please contact support.'
            )

            if site_status == 'suspended':
                html = SUSPENSION_HTML.format(message=message)
                return HttpResponse(html, status=503, content_type='text/html')

            elif site_status == 'maintenance':
                html = MAINTENANCE_HTML.format(message=message)
                return HttpResponse(html, status=503, content_type='text/html')

        return self.get_response(request)

    def _get_status(self):
        """Fetch site status from the JamiiTek API (cached for 5 minutes)."""
        cached = cache.get(self.CACHE_KEY)
        if cached is not None:
            return cached

        try:
            url = f"{self.api_url.rstrip('/')}/{self.api_key}/"
            resp = requests.get(url, timeout=3)
            if resp.status_code == 200:
                data = resp.json()
                cache.set(self.CACHE_KEY, data, self.CACHE_TIMEOUT)
                return data
        except Exception as e:
            logger.warning(f"JamiiTek: Could not reach status API: {e}")

        return None


def is_feature_enabled(request, feature_key):
    """
    Helper to check whether a specific feature is enabled for this site.

    Usage in views:
        from jamiitek_middleware import is_feature_enabled

        def my_view(request):
            if not is_feature_enabled(request, 'ecommerce'):
                return HttpResponse("This feature is not available.")
            ...

    Returns True by default if the feature is not listed (fail-open).
    """
    features = getattr(request, 'jamiitek_features', {})
    return features.get(feature_key, True)