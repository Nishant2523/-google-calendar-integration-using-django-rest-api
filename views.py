Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
... from google.auth.transport import requests
... from google.oauth2 import id_token
... from google.auth import exceptions
... from django.http import JsonResponse
... from django.conf import settings
... from django.views import View
... 
... 
... class GoogleCalendarInitView(View):
...     def get(self, request):
...         redirect_uri = request.build_absolute_uri('/rest/v1/calendar/redirect/')
...         auth_url, _ = settings.GOOGLE_OAUTH2_CLIENT.authorization_url(redirect_uri=redirect_uri)
...         return JsonResponse({'auth_url': auth_url})
... 
... 
... class GoogleCalendarRedirectView(View):
...     def get(self, request):
...         code = request.GET.get('code')
...         redirect_uri = request.build_absolute_uri('/rest/v1/calendar/redirect/')
...         try:
...             token_response = settings.GOOGLE_OAUTH2_CLIENT.fetch_token(
...                 token_url='https://oauth2.googleapis.com/token',
...                 authorization_response=request.build_absolute_uri(),
...                 code=code,
...                 client_secret=settings.GOOGLE_OAUTH2_CLIENT_SECRET,
...                 redirect_uri=redirect_uri,
...             )
...             access_token = token_response.get('access_token')
...             event_list = self.get_event_list(access_token)
...             return JsonResponse({'event_list': event_list})
...         except exceptions.GoogleAuthError:
...             return JsonResponse({'error': 'Failed to fetch access token'})
... 
...     def get_event_list(self, access_token):
...         try:
            id_info = id_token.verify_oauth2_token(
                access_token, requests.Request(), settings.GOOGLE_OAUTH2_CLIENT_ID
            )
            user_id = id_info['sub']
           
            event_list = []  
            return event_list
        except (ValueError, exceptions.GoogleAuthError):
            return []
