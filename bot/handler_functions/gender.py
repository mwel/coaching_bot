# imports
from telegram import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Update)
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
def gender(update: Update, context: CallbackContext) -> int:

    logger.info(f'Gender choice of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    # write data to db
    if update.message.text == 'Gentleman':
        insert_update(update.message.from_user.id, 'gender', 'male')
    elif update.message.text == 'Lady':
        insert_update(update.message.from_user.id, 'gender', 'female')
    else:

        print ('gender.py line 29')

        insert_update(update.message.from_user.id, 'gender', 'diverse')

        print ('gender.py line 33')

    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name}! ' + states.MESSAGES[states.BIRTHDATE],
        #reply_markup=ReplyKeyboardMarkup(
        #    reply_keyboard,
        #    one_time_keyboard=True,
        #    input_field_placeholder='DD.MM.YYYY'),
        # reply_markup=ReplyKeyboardRemove(),
        # TODO: KeyboardButton(str, ...) # date picker for birthday
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIRTHDATE)
    return states.BIRTHDATE
