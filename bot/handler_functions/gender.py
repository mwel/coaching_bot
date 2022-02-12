""" cancel handler function. called, when user enters /cancel """

# imports
from telegram import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def gender(update: Update, context: CallbackContext) -> int:

    user_id = update.message.from_user.id

    logger.info(f'+++++ Gender choice of user {user_id}: {update.message.text} +++++')

    # write data to db
    if update.message.text == 'Gentleman':
        insert_update(user_id, 'gender', 'male')
    elif update.message.text == 'Lady':
        insert_update(user_id, 'gender', 'female')
    else:
        insert_update(user_id, 'gender', 'diverse')

    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name}! ' + \
        states.MESSAGES[states.BIRTHDATE],
        # reply_markup=states.KEYBOARD_MARKUPS[states.BIRTHDATE], # TODO: reactivate once debugged 
        reply_markup=ReplyKeyboardRemove(),
        )

    # save state to DB
    insert_update(user_id, 'state', states.BIRTHDATE)
    return states.BIRTHDATE


# Skips this information and continues on to the next state
def skip_gender(update: Update, context: CallbackContext) -> int:

    user_id = update.message.from_user.id

    logger.info(f'00000 No gender submitted by {user_id} 00000')

    update.message.reply_text(
        'Alright. It\'s just for the letter head. \n'
        'Here, you can be whatever you like. Instead, we want to help you get to where you wanna be!',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.BIRTHDATE],
        # reply_markup=states.KEYBOARD_MARKUPS[states.BIRTHDATE], # TODO: reactivate once debugged 
        reply_markup=ReplyKeyboardRemove(),
        )    

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIRTHDATE)
    return states.BIRTHDATE