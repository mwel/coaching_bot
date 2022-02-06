""" Creating an appointment at the end of the user journey. """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector.select_db import get_value
from handler_functions.calendar.calendar_manager import make_appointment
import datetime


# Stores the photo and asks for a location.
def appointment(update: Update, context: CallbackContext) -> int:

    first_name = get_value(update.message.from_user.id, 'first_name')
    last_name = get_value(update.message.from_user.id, 'last_name')
    email = get_value(update.message.from_user.id, 'email')
    telephone = get_value(update.message.from_user.id, 'telephone')

    summary = 'wavehoover | Coaching Session'
    
    chosen_slot = update.message.text
        
    dt_chosen_slot = datetime.strptime(chosen_slot, '%d/%m/%yT%H:%M:%S')
    iso_slot_start = str(dt_chosen_slot + '+01:00')
    print(f'>>>>> ISO_SLOT_START: {iso_slot_start}')

    slot_end = chosen_slot + datetime.timedelta(minutes=50)
    dt_slot_end = datetime.strptime(slot_end, '%d/%m/%yT%H:%M:%S')
    iso_slot_end = str(dt_slot_end + '+01:00')
    print(f'>>>>> ISO_SLOT_END: {iso_slot_end}')

    # build the event data into the event object
    event = {
        f'summary': summary,
        'location': 'Phone Call',
        'description': f'Your coach will call you under the following number: {telephone}',
        'start': {
            'dateTime': iso_slot_start,
        },
        'end': {
            'dateTime': iso_slot_end,
            # 'timeZone': 'Europe/Zurich',
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
    
    make_appointment(event) # hand over user info to make appointment
    insert_update(update.message.from_user.id, 'appointment', chosen_slot)
    logger.info(f'+++++ User {update.message.from_user.first_name} MADE APPOINTMENT AT: {chosen_slot} +++++')
    
    update.message.reply_text(
        'Splendid! You should receive a calendar appointment shortly.\n' 
        f'Your coach will call you on {chosen_slot} under the following number: {telephone}\n'
        'In case of any questions, please don\'t hesitate to get in touch!\n'
        'Looking forward to our session!\n'
        'Your wavehoover team',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    insert_update(update.message.from_user.id, 'state', states.COMPLETED)
    return ConversationHandler.END


# Skips the photo and asks for a location.
def skip_appointment(update: Update, context: CallbackContext) -> int:
    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} does not want to make an appointment.')
    insert_update(update.message.from_user.id, 'appointment', 'None')
    
    update.message.reply_text(
        'Alright - you can get in touch with us at any time, if you want to.\n'
        'See you around.\n'
        'Your wavehoover team',
        reply_markup=ReplyKeyboardRemove(),
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.COMPLETED)
    return ConversationHandler.END
