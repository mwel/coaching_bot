# imports
from telegram import (ReplyKeyboardMarkup, KeyboardButton, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# TODO: Keyboard for next state
reply_keyboard = 'email keyboard'

# replymarkup_variable for next state
custom_keyboard=ReplyKeyboardMarkup(
    reply_keyboard, 
    one_time_keyboard=True, 
    input_field_placeholder='mybest@address.com'
    )


# Stores the information received and continues on to the next state
def birthdate(update: Update, context: CallbackContext) -> int:
    logger.info(f'Birthdate of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    insert_update(update.message.from_user.id, 'birthdate', update.message.text)

    update.message.reply_text(
        f'Great age!\n\n'
        'Now, send me your email address, so I can send you your summary of submitted data upon completion.'
        'WARNING: You can /skip this step, but if you do, I cannot send you a summary and confirmation of your request.',
        # TODO: reply_markup=custom_markup
        # )
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL


# Skips this information and continues on to the next state
def skip_birthdate(update: Update, context: CallbackContext) -> int:
    logger.info(f'No birthdate submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    # insert_update(update.message.from_user.id, 'birthdate', '0')

    update.message.reply_text(
        f'I wouldn\'t want to talk about my age either... ;)\n\n'
        'Now, send me your email address, so I can send you your summary of submitted data upon completion.'
        'WARNING: You can /skip this step, but if you do, I cannot send you a summary and confirmation of your request.',
        # TODO: reply_markup=custom_markup
        # )
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL