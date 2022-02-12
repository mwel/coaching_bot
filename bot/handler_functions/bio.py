""" bio handler function. called, when user arrives at bio state """

# imports
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def bio(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id
    bio_message = update.message.text
    
    logger.info(f'+++++ Bio of user {user_id}: {bio_message} +++++')

    # write bio to DB
    insert_update(user_id, 'bio', bio_message)

    # reply keyboard for next state
    update.message.reply_text(
        'What a story! We will definately pick that up in our first session!\n\n' + \
        'Ok - now let\'s get some basics down: \n' + \
        states.MESSAGES[states.GENDER],
        reply_markup=states.KEYBOARD_MARKUPS[states.GENDER],
        )

    # save state to DB
    insert_update(user_id, 'state', states.GENDER)
    return states.GENDER


# Skips this information and continues on to the next state
def skip_bio(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id

    logger.info(f'00000 No bio submitted by {user_id} 00000')

    # alternative message
    update.message.reply_text(
        'Alright. No problem. I know, it can be uneasy to share at first. If you would like, I can offer you a free "gettin to know each other" phone call once you have finished the sign up.',
        reply_markup=ReplyKeyboardRemove(),
        )

    # reply keyboard for next state
    update.message.reply_text(
        states.MESSAGES[states.GENDER],
        reply_markup=states.KEYBOARD_MARKUPS[states.GENDER],
        )    

    # save state to DB
    insert_update(user_id, 'state', states.GENDER)
    return states.GENDER
