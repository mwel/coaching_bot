# imports
from telegram import (ReplyKeyboardMarkup, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update

# gender copy variables
male = 'Gentleman'
female = 'Lady'
other = 'Unicorn'

# Stores the information received and continues on to the next state
def bio(update: Update, context: CallbackContext) -> int:
    logger.info(f'+++++ Bio of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text} +++++')
    
    # write bio to DB
    insert_update(update.message.from_user.id, 'bio', update.message.text)

    # create keyboard for next question >> GENDER
    reply_keyboard = [[female, male, other]]

    update.message.reply_text(
        'What a story! We will definately pick that up in our first session!\n\n'
        'Ok - now let\'s get some basics down: \n'
        'Would you like to be referred to as lady, gentleman or unicorn?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Lady? Gentleman? Unicorn?'
            )
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.GENDER)
    return states.GENDER