""" simple tests for data base and handler functions """

# data base tests
from handler_functions.database_connector.create_db import create_db
from handler_functions.database_connector.insert_value_db import insert_update
# from handler_functions.database_connector import select_db
# from handler_functions import states
# from handler_functions import help
from handler_functions.calendar.generate_ics import generate_ics

from datetime import datetime, timedelta
from handler_functions.calendar.calendar_manager import make_appointment

# insert_update_db.insert_update(
#     user_id=123456789,
#     first_name='Michael',
#     last_name='Müller',
#     gender='male',
#     photo='01010101010101010101',
#     birthdate='19900101',
#     email='test@gmx.de',
#     phone='+41123456789',
#     longitude='65432345678.00',
#     latitude='65432345678.00',
#     bio = 'Ich wurde als Phritte gebohren. Doch also selche krepieren soll ich nicht!',
#     state = '-1'
#     )

# create_db()

# insert_update(123456789, 'first_name', 'Tüb')

# select_db.get_all_data(28648774)

# single selects for all db colum value types
# select_db.get_value(28648774, 'first_name')
# select_db.get_value(28648774, 'last_name')
# select_db.get_value(28648774, 'gender')
# select_db.get_value(28648774, 'photo')
# select_db.get_value(28648774, 'birthdate')
# select_db.get_value(28648774, 'email')
# select_db.get_value(28648774, 'telephone')
# select_db.get_value(28648774, 'longitude')
# select_db.get_value(28648774, 'latitude')
# select_db.get_value(28648774, 'bio')
# select_db.get_value(28648774, 'state')

# select_db.user_search(28648774)

# print (states.GENDER)

# help.help()

# test calendar function
# generate_ics(
#     coachee_name='Maria', 
#     coachee_email='mgw.longwave@gmail.com', 
#     coachee_phone_number='+41123456789',
#     coach_name='Coach', 
#     coach_email='max@wavehoover.com', 
#     year = 2022,
#     month = 1,
#     day =1,
#     start_hour=9,
#     start_minute=0, 
#     end_hour=10,
#     end_minute=0, 
#     )



#   0     user_id INTEGER PRIMARY KEY,
#   1     time_stamp TEXT,
#   2     first_name TEXT,
#   3     last_name TEXT,
#   4     gender TEXT,
#   5     photo BLOB,
#   6     birthdate INTEGER,
#   7     email TEXT UNIQUE,
#   8     telephone TEXT UNIQUE,
#   9     longitude INTEGER,
#   10    latitude INTEGER,
#   11    bio TEXT,
#   12    state INTEGER,
#   13    mail_sent BOOLEAN,
#   14    appointment TEXT


# make appointment

email = 'mgw.longwave@gmail.com'
telephone = '0041792789561'

# write data to db

summary = 'wavehoover | Coaching Session'

slot_start = '2022-02-07 15:00:00'
dt_slot_start = datetime.strptime(slot_start, '%Y-%m-%d %H:%M:%S') # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
iso_slot_start = str(dt_slot_start.isoformat('T') + '+01:00')
print(f'>>>>> ISO_SLOT_START: {iso_slot_start}')

slot_end = str(dt_slot_start + timedelta(minutes=50))
dt_slot_end = datetime.strptime(slot_end, '%Y-%m-%d %H:%M:%S')
iso_slot_end = str(dt_slot_end.isoformat('T') + '+01:00')
print(f'>>>>> ISO_SLOT_END: {iso_slot_end}')

event = {
    f'summary': summary,
    'location': 'Phone Call',
    'description': f'Your coach will call you under the following number: {telephone}',
    'start': {
        'dateTime': iso_slot_start,
        'timeZone': 'Europe/Berlin',
    },
    'end': {
        'dateTime': iso_slot_end,
        'timeZone': 'Europe/Berlin',
    },
    # 'recurrence': [
        #'RRULE:FREQ=DAILY;COUNT=2'
    # ],
    'attendees': [
        {'email': email},
    ],
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 60},
        ],
    },
    }

make_appointment(event)