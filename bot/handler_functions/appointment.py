""" Creating an appointment at the end of the user journey. """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector.select_db import get_value
from handler_functions.calendar.calendar_manager import make_appointment
from datetime import datetime, timedelta
from uuid import uuid1
from random import randint, random


# Stores the photo and asks for a location.
def appointment(update: Update, context: CallbackContext) -> int:

    user_id = update.message.from_user.id

    first_name = get_value(user_id, 'first_name')
    last_name = get_value(user_id, 'last_name')
    email = get_value(user_id, 'email')
    telephone = get_value(user_id, 'telephone')

    summary = 'wavehoover | Coaching Session'
    
    slot_start = update.message.text
    dt_slot_start = datetime.strptime(slot_start, '%Y-%m-%d %H:%M:%S') # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    iso_slot_start = str(dt_slot_start.isoformat('T') + '+01:00')
    logger.info(f'>>>>> ISO_SLOT_START: {iso_slot_start}')

    slot_end = str(dt_slot_start + timedelta(minutes=50))
    dt_slot_end = datetime.strptime(slot_end, '%Y-%m-%d %H:%M:%S')
    iso_slot_end = str(dt_slot_end.isoformat('T') + '+01:00')
    logger.info(f'>>>>> ISO_SLOT_END: {iso_slot_end}')

    uuid = str(str(user_id) + str(randint(10000, 99999)))
    logger.info(f'>>>>> UUID for user_id {user_id}: {uuid}')

    # build the event data into the event object
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
        'id': uuid,
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
    
    make_appointment(user_id, slot_start, event) # hand over user info to make appointment
    insert_update(user_id, 'appointment', slot_start)
    insert_update(user_id, 'event_id', uuid)
    logger.info(f'+++++ User {update.message.from_user.first_name} MADE APPOINTMENT AT: {slot_start} +++++')
    
    update.message.reply_text(
        'Splendid! You should receive a calendar appointment shortly.\n' 
        f'Your coach will call you on {slot_start} under the following number: {telephone}\n'
        'In case of any questions, please don\'t hesitate to get in touch!\n'
        'Looking forward to our session!\n'
        'Your wavehoover team',
        reply_markup=ReplyKeyboardRemove(),
    )
    update.message.reply_text(
        'In case you would like to cancel your appointment, please do so in your calendar OR enter /cancel_appointment\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # insert_update(user_id, 'state', 10)
    # return states.COMPLETED
    return ConversationHandler.END


# Skips the photo and asks for a location.
def skip_appointment(update: Update, context: CallbackContext) -> int:

    user_id = update.message.from_user.id

    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} does not want to make an appointment.')
    insert_update(user_id, 'appointment', 'None')
    
    update.message.reply_text(
        'Alright - you can get in touch with us at any time, if you want to.\n'
        'See you around.\n'
        'Your wavehoover team',
        reply_markup=ReplyKeyboardRemove(),
        )

    # save state to DB
    # insert_update(user_id, 'state', 10)
    return ConversationHandler.END
