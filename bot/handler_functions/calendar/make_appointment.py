""" Generates a .ics file, that can be imported to any calendar"""

# imports
from datetime import datetime
import pytz
from icalendar import Calendar, Event
from pathlib import Path
import os

def make_appointment (coachee_name, coachee_email, coach_name, coach_email, year, month, day, start_hour, start_minute, end_hour, end_minute):

    # when the meeting should start
    start_time = datetime(year, month, day, start_hour, start_minute, 0, tzinfo=pytz.utc) # replace with start parameter

    # when the meeting should end
    end_time = datetime(year, month, day, end_hour, end_minute, 0, tzinfo=pytz.utc) # replace with end parameter
    
    # small note to put in the appointment
    message = f'Coaching sessiong between {coachee_name} and {coach_name}. Your coach will call you on your phone.'

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