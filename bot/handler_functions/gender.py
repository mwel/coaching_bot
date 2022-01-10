# imports
from telegram import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def gender(update: Update, context: CallbackContext) -> int:

    # reply keyboard for next state
    reply_keyboard = [['Gentleman', 'Lady', 'Unicorn']]
    update.message.reply_text(
        'Ok - now let\'s get some basics down: \n'
        'Would you like to be referred to as lady, gentleman or unicorn?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Lady? Gentleman? Unicorn? ... here you can be whatever you want.'
        )
    )

    logger.info(f'Gender choice of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')
    
    # write data to db
    if update.message.text == 'Gentleman':
        insert_update(update.message.from_user.id, 'gender', 'male')
    elif update.message.text == 'Lady':
        insert_update(update.message.from_user.id, 'gender', 'female')
    else:
        insert_update(update.message.from_user.id, 'gender', 'diverse') 

    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIRTHDATE)
    return states.BIRTHDATE