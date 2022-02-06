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
import time


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials_directory = os.path.join('calendar_credentials', 'credentials.json')

# reference to the ID of the calendar to be connected
coaching_calendar_ID = '84qo0c5ctm3e6p2cioh2c11iqc@group.calendar.google.com'



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
    
    print(f'+++++ SLOT START: {start}') # must be in format RFC3339, i.e. 1985-04-12T23:20:50.52Z
    print(f'+++++ SLOT END: {end}')

    start_iso = str(start.isoformat('T')+'+01:00') # convert UTC to CET for the request.
    print(f'+++++ start_iso: {start_iso}')

    end_iso = str(end.isoformat('T')+'+01:00') # same for end time
    print(f'+++++ end_iso: {end_iso}')

    request = {
        "timeMin": start_iso,
        "timeMax": end_iso,
        "timeZone": "Europe/Berlin", # input time zone to let API know to convert to CET for the response
        "items": [
            {
            "id": coaching_calendar_ID #put ID incl. the @domain...
            }
        ]
        }

    print (request)
    
    try:
        
        response = service.freebusy().query(body=request).execute()
        print('+++++ CAL: AVAILABILITY CHECKED +++++')
        print('>>>>> HTTP Response' + str(response))
    
        # climb down the dict latter and read the busy response from the HTTP-Response object
        calendars = response.get('calendars')
        print(f'>>>>> CALENDARS: {calendars}')
        calendar_temp = calendars.get(coaching_calendar_ID)
        print(f'>>>>> CALENDAR_TEMP: {calendar_temp}')
        availability = calendar_temp.get('busy')
        print(f'>>>>> AVAILABILITY: {availability}')
        if availability == []:
            return True


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
    round = 0
    while slots < 3:
        round += 1
        end = start + datetime.timedelta(minutes=50)
        
        if (check_availability(start, end)): # TODO: check_availability returns True, if there are obstacles. So 'False' means, we have found a free slot.
            free_slots.append(str(start))
            slots += 1;

            print(f'>>>>> FREE SLOT found at: {start} <<<<<')
            start = dt8 + datetime.timedelta(days=3*slots)

        else: 
            print ('##### NO SLOT FOUND #####')
            start = start + datetime.timedelta(hours=1)
        
        print (f'##### SLOTS: {slots} after ROUND: {round} #####') # tell me, how many rounds the while loop has to run to get 3 slots


    print(f'>> FREE SLOTS: {free_slots}')
    return free_slots




# make an appointment in the calendar
def make_appointment(event):

    service = authenticate()
    # print(f'>>>>> CAL List: {service.calendarList().list()}')

    try:

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