""" manages CRD calendar functions for coaching appointments """

from __future__ import print_function

# default imports
import datetime
from posixpath import dirname

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# custom imports
import os.path
from pathlib import Path
import json
import time
import array


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials_directory = os.path.join('calendar_credentials', 'credentials.json')

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
                credentials_directory, SCOPES)
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
                os.path.join(str(Path(__file__).parent.parent), 'calendar', credentials_directory), SCOPES) # the path here needs to be different from the one in main(), because the directory from which authenticate is called is being used as the reference for the credentials.
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
def check_availability(start, end):

    service = authenticate()
    
    body = {
        "timeMin": str(start),
        "timeMax": str(end),
        # "timeZone": string,
        # "groupExpansionMax": 3,
        # "calendarExpansionMax": 3,
        "items": [
            {
            "id": coaching_calendar_ID
            }
        ]
        }
    
    try:
        
        availability = service.freebusy().query(body=body)
        print('+++++ CAL: AVAILABILITY CHECKED +++++')
        print(availability)
        return availability

    except HttpError as error:
        print('ERROR: %s' % error)


# def business_hours(day, enddate, excluded, working_hours): # i.e. date = datetime.datetime(2021, 9, 01), enddate = datetime.datetime(2022, 2, 28), excluded = (6,7), working_hours=(datetime.time(...9))
    
#     days = []
    
#     while startdate.date() <= enddate.date():
#         if startdate.isoweekday() not in excluded:
#             days.append(day)
#         startdate += datetime.timedelta(days=1)

#     print(business_hours(datetime.datetime(2019, 1, 21),
#                datetime.datetime(2019, 1, 30))

#     return hours




def find_slots():

    # Get today's datetime
    datenow = datetime.datetime.now()

    # Create datetime variable for 8 AM
    dt8 = None

    # If today's hour is < 8 AM
    if datenow.hour < 8:

        # Create date object for today's year, month, day at 8 AM
        dt8 = datetime.datetime(datenow.year, datenow.month, datenow.day, 8, 0, 0, 0)

    # If today is past 6 AM, increment date by 1 day
    else:

        # Get 1 day duration to add
        day = datetime.timedelta(days=1)

        # Generate tomorrow's datetime
        tomorrow = datenow + day

        # Create new datetime object using tomorrow's year, month, day at 6 AM
        dt8 = datetime.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 8, 0, 0, 0)

    # Create timestamp from datetime object
    timestamp = time.mktime(dt8.timetuple())
    
    # within the business hours, find 3 free time slots to suggest to the user
    free_slots = []
    slots = 0
    start = dt8
    while slots < 3:
        end = dt8 + datetime.timedelta(hours=1)
        
        if (check_availability(str(start), str(end))): # TODO: fix availability check!
            free_slots.append(str(start))
            slots += 1;

            print(f'>> FREE SLOT FOUND: {start}')
            start = start + datetime.timedelta(days=2)

        else: 
            start = end


    print(f'>> FREE SLOTS: {free_slots}')
    return free_slots




# make an appointment in the calendar
def make_appointment(body):

    service = authenticate()
    
    try:
    
        appointment = service.event().insert(calendarId=coaching_calendar_ID, body=body)
        print(appointment)

        event = service.events().insert(calendarId=coaching_calendar_ID, body=event).execute()
        print('+++++ CAL: APPOINTMENT MADE: %s' % (event.get('htmlLink')))
        return event

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