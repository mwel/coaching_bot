# imports
from telegram import (ReplyKeyboardMarkup, KeyboardButton, Update)
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def email(update: Update) -> int:
    logger.info(f'Email address of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    insert_update(update.message.from_user.id, 'email', update.message.text)

    reply_keyboard = KeyboardButton(str, request_contact=True),
    update.message.reply_text(
        f'Great age!\n\n'
        'Now, send me your email address, so I can send you your summary of submitted data upon completion.',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder='+49 123 456 78')
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.TELEPHONE)
    return states.TELEPHONE


# Skips this information and continues on to the next state
def skip_email(update: Update) -> int:
    logger.info(f'No email address submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        'Sorry, without an email address, the onboarding cannot be finished. Please enter one or /cancel'
        'WARNING: If you cancel, all your previously submitted data will be deleted and you have to start over.',
        reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder='mybest@address.com')
    )
    # Looping back to state: EMAIL (we do not want to save anything to the db as we want to user to submit an email) 
    return states.EMAIL
    
