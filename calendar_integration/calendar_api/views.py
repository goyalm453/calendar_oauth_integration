from google.oauth2 import credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View

class GoogleCalendarInitView(View):
    def get(self, request):
        # Set up the OAuth2 flow
        flow = InstalledAppFlow.from_client_secrets_file(
            '/path/to/client_secret.json',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
             redirect_uri=['http://localhost:8000/rest/v1/calendar/init/'],
        )
        authorization_url, state = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
        )
        
        request.session['oauth_state'] = state
        return redirect(authorization_url)

class GoogleCalendarRedirectView(View):
    def get(self, request):
        # Verify the state to prevent cross-site request forgery
        if request.GET.get('state') != request.session.get('oauth_state'):
            return HttpResponse('Invalid state parameter', status=400)
        
        
        flow = InstalledAppFlow.from_client_secrets_file(
            '/path/to/client_secret.json',
            scopes=['https://www.googleapis.com/auth/calendar.readonly'],
            redirect_uri=['http://localhost:8000/rest/v1/calendar/redirect'],
        )
        flow.fetch_token(
            authorization_response=request.build_absolute_uri(),
        )
        credentials = flow.credentials

        # Create a service object to interact with the Google Calendar API
        service = build('calendar', 'v3', credentials=credentials)

        # Retrieve a list of events from the user's calendar
        events_result = service.events().list(calendarId='primary', maxResults=10).execute()
        events = events_result.get('items', [])
        
        
        return HttpResponse(events)
