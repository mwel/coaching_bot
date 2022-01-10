# imports
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def location(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name} - let\'s continue... '
        'I\'m from Switzerland. It\'s really nice here! Where are you from?\n\n'
        '- > Tip: Use Telegram\'s built in function to share your location with me.\n\n',
        reply_markup=ReplyKeyboardRemove(),
    )

    insert_update(update.message.from_user.id, 'latitude', update.message.location.latitude)
    insert_update(update.message.from_user.id, 'longitude', update.message.location.longitude)

    logger.info(f'+++++ Location of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.location.latitude} , {update.message.location.longitude} +++++')
    
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime.',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO


# Skips this information and continues on to the next state
def skip_location(update: Update, context: CallbackContext) -> int:
    
    logger.info(f'+++++ No location submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}. +++++')

    update.message.reply_text(
        'No matter where you are, coaching will get you to the next level!',
        reply_markup=ReplyKeyboardRemove(),
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO
