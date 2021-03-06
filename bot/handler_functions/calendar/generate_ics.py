""" Generates a .ics file, that can be imported to any calendar"""

# imports
from datetime import datetime
from icalendar import Calendar, Event
from pathlib import Path

import os

# find an appointment for a coaching session
def find_appointment (calendar, year, month, day, start_hour, start_minute):

    # TODO: Call Google Calendar API
    event = 'event' # TODO: Change to API response

    return event


# generate an ics file to be attached to an email to the coachee
def generate_ics (coachee_name, coachee_email, coachee_phone_number, coach_name, coach_email, year, month, day, start_hour, start_minute, end_hour, end_minute): # TODO: remove date and time and move functionality to find appointment function

    # when the meeting should start
    start_time = datetime(year, month, day, start_hour, start_minute, 0) # if you want to operate in multiple time zones: check out pytz

    # when the meeting should end
    end_time = datetime(year, month, day, end_hour, end_minute, 0)
    
    # appointment title
    summary = f'wavehoover | 1:1 Coaching Session'

    # small note to put in the appointment
    description = f'Coaching sessiong between {coachee_name} and {coach_name}. Your coach will call you via the number you have provided: {coachee_phone_number}. Please let your coach know, if you cannot take the appointment or would like to reschedule. Thanks!'


    # create a calendar object and add the attendees - in this case the coach and the coachee
    cal = Calendar()
    cal.add('attendee', f'MAILTO:{coachee_email}')
    cal.add('organizer', f'MAILTO:{coach_email}')

    # create and configute the appointment / event
    event = Event()
    event.add('summary', summary)
    event.add('description', description)
    event.add('location', 'Phone Call')
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    event.add('dtstamp', datetime(year, month, day, 0, 0, 0))

    # add events to calendar
    cal.add_component(event)
    print ('#### Event:')
    print(event)

    print('#### Calendar')
    print(cal)

    # define, where to put the file
    directory = str(Path(__file__).parent.parent.parent.parent) # TODO: figure out how to write ics to 'appointments'-folder and how to attach it to the email
    
    # open the file
    f = open(os.path.join(directory, 'appointments', 'wavehoover - Personal Coaching Appointment.ics'), 'wb')
    
    # write calendar invite data to file
    f.write(cal.to_ical())

    # confirm
    print (f'+++++ SUCCESS: file generated and saved here: {directory} +++++')
    
    #close
    f.close()

    return event

