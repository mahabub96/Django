# books/middleware.py

import time
from django.core.cache import cache

class CacheGETMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            cache_key = f"cache_{request.get_full_path()}"
            response = cache.get(cache_key)
            if response:
                return response

        response = self.get_response(request)
        cache.set(cache_key, response, timeout=300)  # Cache for 5 minutes
        return response
