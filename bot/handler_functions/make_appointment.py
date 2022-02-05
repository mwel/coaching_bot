""" Creating an appointment at the end of the user journey. """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
from calendar_manager import make_appointment


# Stores the photo and asks for a location.
def appointment(update: Update, context: CallbackContext) -> int:

    logger.info(f'+++++ User {update.message.from_user.first_name} MAKING APPOINTMENT +++++')

    first_name = select_db.get_value(update.message.from_user.id, 'first_name')
    last_name = select_db.get_value(update.message.from_user.id, 'last_name')
    email = select_db.get_value(update.message.from_user.id, 'email')
    telephone = select_db.get_value(update.message.from_user.id, 'telephone')


    # confirmation message
    update.message.reply_text(
        states.MESSAGES[states.APPOINTMENT],
        reply_markup=states.KEYBOARD_MARKUPS[states.APPOINTMENT],
        )

    make_appointment() # hand over user info to make appointment
    

    return ConversationHandler.END
