""" bio handler function. called, when user arrives at bio state """

# imports
from telegram import Update
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def bio(update: Update, context: CallbackContext) -> int:
    logger.info(f'+++++ Bio of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text} +++++')

    # input validation
    

    # write bio to DB
    insert_update(update.message.from_user.id, 'bio', update.message.text)

    # reply keyboard for next state
    update.message.reply_text(
        'What a story! We will definately pick that up in our first session!\n\n' + \
        'Ok - now let\'s get some basics down: \n' + \
        states.MESSAGES[states.GENDER],
        reply_markup=states.KEYBOARD_MARKUPS[states.GENDER],
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.GENDER)
    return states.GENDER
