""" Generates a .ics file, that can be imported to any calendar"""

# imports
from icalendar import Calendar, Event
import pytz
from datetime import datetime
import os
from pathlib import Path

def make_appointment (coachee_name, coachee_email, coach_name, coach_email, start, end):

    # when the meeting should start
    start_time = datetime(2021, 4, 4, 8, 0, 0, tzinfo=pytz.utc) # replace with start parameter

    # when the meeting should end
    end_time = datetime(2021, 4, 4, 10, 0, 0, tzinfo=pytz.utc) # replace with end parameter
    
    # small note to put in the appointment
    message = ''

    # create a calendar object and add the attendees - in this case the coach and the coachee
    cal = Calendar()
    cal.add(coachee_name, f'MAILTO:{coachee_email}')
    cal.add(coach_name, f'MAILTO:{coach_email}')

    # create and configute the appointment / event
    event = Event()
    event.add('summary', f'Your first coaching session with {coach_name}')
    event.add('dtstart', start_time)
    event.add('dtend', end_time)
    event.add('dtstamp', datetime(2021, 4, 4, 0, 10, 0, tzinfo=pytz.utc))

    # add events to calendar
    cal.add_component(event)

    # execute
    directory = str(Path(__file__).parent.parent) + "/"
    print(directory)
    f = open(os.path.join(directory, 'example.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()