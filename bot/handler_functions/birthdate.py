# imports
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, Update, replykeyboardremove)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# reply keyboard for next state
reply_keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['/', '0', '.']
    ],


# Stores the information received and continues on to the next state
def birthdate(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name}, '
        'tell me - when is your birthday?',
        #reply_markup=ReplyKeyboardMarkup(
        #    reply_keyboard, 
        #    one_time_keyboard=True, 
        #    input_field_placeholder='DD.MM.YYYY'),
        # reply_markup=ReplyKeyboardRemove(),
        # TODO: KeyboardButton(str, ...) # date picker for birthday
    )
    
    logger.info(f'Birthdate of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    insert_update(update.message.from_user.id, 'birthdate', update.message.text)

    update.message.reply_text(
        'Great age!\n\n'
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL


# Skips this information and continues on to the next state
def skip_birthdate(update: Update, context: CallbackContext) -> int:
    logger.info(f'No birthdate submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        'I wouldn\'t want to talk about my age either... ;)\n\n'
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL
