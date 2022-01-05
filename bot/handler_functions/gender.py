# imports
from telegram import (ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, Update)
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def gender(update: Update) -> int:
    logger.info(f'Gender choice of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')
    
    # write data to db
    if update.message.text == 'Gentleman':
        insert_update(update.message.from_user.id, 'gender', 'male')
    elif update.message.text == 'Lady':
        insert_update(update.message.from_user.id, 'gender', 'female')
    else:
        insert_update(update.message.from_user.id, 'gender', 'diverse') 

    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name}!'
        'Tell me, when is your birthday?',
        # TODO: KeyboardButton(str, ...) # date picker for birthday
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIRTHDAY)
    return states.BIRTHDAY