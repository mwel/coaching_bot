from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


from handler_functions.database_connector.insert_value_db import insert_update


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# reference to the ID of the calendar to be connected
coaching_calendar_ID = '84qo0c5ctm3e6p2cioh2c11iqc'



def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'bot/constants/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    except HttpError as error:
        print('ERROR: %s' % error)



def authenticate():
    """ Authenticate to Google Calendar API """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'bot/constants/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        print('+++++ OAuth2 SUCCESSFUL +++++')
       
    except HttpError as error:
        print('ERROR: %s' % error)

    return service



# check, when there is a free slot in the calendar
def check_availability():

    service = authenticate()
        
    try:
    
        availability = service.freebusy().query()
        print('+++++ CAL: AVAILABILITY CHECKED +++++')
        print(availability)
        return availability

    except HttpError as error:
        print('ERROR: %s' % error)



# make an appointment in the calendar
def make_appointment(user_id, body):

    service = authenticate()
    
    try:
    
        appointment = service.event().insert(calendarId=coaching_calendar_ID, body=body)
        print('+++++ CAL: APPOINTMENT MADE +++++')
        print(appointment)
        insert_update(user_id, 'appointment', appointment)

        return appointment


    except HttpError as error:
        print('ERROR: %s' % error)



# cancel / delete an appointment from the calendar
def cancel_appointment():

    service = authenticate()

    try:
        
        service.event().delete()
        print('+++++ CAL: APPOINTMENT CANCELED +++++')

    except HttpError as error:
        print('ERROR: %s' % error)



if __name__ == '__main__':
    main()