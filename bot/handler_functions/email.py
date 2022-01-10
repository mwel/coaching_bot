""" email handler function. called, when user arrives at email state """

# imports
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update)
from telegram.ext import CallbackContext
from bot.handler_functions.states import EMAIL, MESSAGES
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def email(update: Update, context: CallbackContext) -> int:
    logger.info(f'Email address of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    # TODO: data validation email address

    insert_update(update.message.from_user.id, 'email', update.message.text)

    update.message.reply_text(
        'Ok - I will send you a summary, once we have completed sign up.',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.TELEPHONE],
        reply_markup=states.KEYBOARD_MARKUPS[states.TELEPHONE],
        )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.TELEPHONE)
    return states.TELEPHONE


# Skips this information and continues on to the next state
def skip_email(update: Update, context: CallbackContext) -> int:
    logger.info(f'No email address submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        states.MESSAGES[states.EMAIL_OR_EXIT],
        reply_markup=states.KEYBOARD_MARKUPS[states.EMAIL_OR_CANCEL],
        )
            # Looping back to state: EMAIL (we do not want to save anything to the db as we want to user to submit an email) 
    return states.EMAIL
    
