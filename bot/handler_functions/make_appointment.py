""" Creating an appointment at the end of the user journey. """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_update_db import insert_update
from handler_functions.database_connector.select_db import get_value
from handler_functions.calendar.calendar_manager import check_availability, make_appointment


# Stores the photo and asks for a location.
def appointment(update: Update, context: CallbackContext) -> int:

    first_name = get_value(update.message.from_user.id, 'first_name')
    last_name = get_value(update.message.from_user.id, 'last_name')
    email = get_value(update.message.from_user.id, 'email')
    telephone = get_value(update.message.from_user.id, 'telephone')

    slot1 = states.slot1
    slot2 = states.slot2
    slot3 = states.slot3

    # write data to db
    if update.message.text == slot1:
        chosen_slot = slot1

    elif update.message.text == slot2:
        chosen_slot = slot2

    elif update.message.text == slot3:
        chosen_slot = slot3

    else:
        update.message.reply_text(
        f'No appointment was made.', 
        reply_markup=ReplyKeyboardRemove(),
        )
    

    insert_update(update.message.from_user.id, 'appointment', chosen_slot)
    make_appointment() # hand over user info to make appointment
    logger.info(f'+++++ User {update.message.from_user.first_name} MADE APPOINTMENT AT: {chosen_slot} +++++')

    date = chosen_slot
    
    update.message.reply_text(
        f'Splendid! Your coach will call you on {date}, at {time} under the following number: {telephone}'
        'Looking forward to our session!'
        'Your wavehoover team',
        reply_markup=ReplyKeyboardRemove(),
    )

    return ConversationHandler.END
