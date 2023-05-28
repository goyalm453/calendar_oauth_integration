# calendar_oauth_integration
In this assignment you have to implement google calendar integration using django rest api. You need to use the OAuth2 mechanism to get users calendar access. Below are detail of API endpoint and corresponding views which you need to implement
For run this project on a local machine:

Create virtual environment

# Install the required dependencies:
pip install -r requirements.txt

Set up Google API credentials:

# Go to the Google Developers Console.
Create a new project or select an existing one.
Enable the "Calendar API" for your project.
Create OAuth 2.0 credentials and download the client secrets JSON file.
Move the client secrets JSON file to the project directory.
# Configure Django settings:

Open the settings.py file in the project folder.
Update the DATABASES configuration to connect to your database.
Set the SECRET_KEY with a secure secret for your application.
# Apply the database migrations:
python manage.py migrate
# Run the Django development server:
python manage.py runserver
# API Endpoints
GET /rest/v1/calendar/init/: Initiates the OAuth2 flow and prompts the user for their Google account credentials.

GET /rest/v1/calendar/redirect/: Handles the redirect request from Google after authorization. It exchanges the authorization code for an access token and retrieves a list of events from the user's Google Calendar.

# Note: To run this assignment need google account credentials which need to save in the project directory and add a redirect URL in your google cloud

# Acknowledgements
This project was built using the following technologies and libraries:

Django: Web framework for building the REST API

Google Calendar API: Used to integrate with the user's Google Calendar

Google OAuth 2.0: Used for user authentication and authorization
Contact
