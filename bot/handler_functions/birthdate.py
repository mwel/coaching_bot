""" birthdate handler function. called, when user arrives at birthdate state """

# imports
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, Update, replykeyboardremove)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def birthdate(update: Update, context: CallbackContext) -> int:
    logger.info(f'Birthdate of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    insert_update(update.message.from_user.id, 'birthdate', update.message.text)

    update.message.reply_text(
        'Great age!\n\n',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.EMAIL],
        reply_markup=states.KEYBOARD_MARKUPS[states.EMAIL],
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL


# Skips this information and continues on to the next state
def skip_birthdate(update: Update, context: CallbackContext) -> int:
    logger.info(f'No birthdate submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    # insert_update(update.message.from_user.id, 'birthdate', '0')

    update.message.reply_text(
        'I wouldn\'t want to talk about my age either... ;)\n\n',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.EMAIL],
        reply_markup=states.KEYBOARD_MARKUPS[states.EMAIL],
        )    

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.EMAIL)
    return states.EMAIL
