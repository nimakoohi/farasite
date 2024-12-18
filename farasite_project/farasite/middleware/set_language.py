import logging
from django.utils import translation

logger = logging.getLogger(__name__)

class SetLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        lang = request.GET.get('lang')
        if lang:
            translation.activate(lang)
            request.session['django_language'] = lang  # Use the new session key
        response = self.get_response(request)
        return response
