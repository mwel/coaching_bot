""" simple tests for data base and handler functions """

# data base tests
# from database_connector import create_db, select_db, insert_update_db, delete_record_db, insert_value_db
from handler_functions.database_connector import select_db
from handler_functions import states
from handler_functions import help
from handler_functions.calendar.generate_ics import generate_ics
from calendar_manager import authenticate

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

# insert_value_db.insert_update(123456789, 'first_name', 'Tüb')

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

# test calendar_manager
authenticate()