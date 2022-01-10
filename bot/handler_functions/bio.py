# imports
from os import remove
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def bio(update: Update, context: CallbackContext) -> int:
    logger.info(f'+++++ Bio of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text} +++++')
    
    update.message.reply_text(
        f'Now, {update.message.from_user.first_name} - tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best coaching experience possible.',
        reply_markup=ReplyKeyboardRemove(),
        )

    # write bio to DB
    insert_update(update.message.from_user.id, 'bio', update.message.text)

    # answer to user entry
    update.message.reply_text(
        'What a story! We will definately pick that up in our first session!\n\n',
        reply_markup=ReplyKeyboardMarkup(),
    )


    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.GENDER)
    return states.GENDER