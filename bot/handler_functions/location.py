""" location handler function. called, when user arrives at location state """

# imports
from telegram import Update, ReplyKeyboardRemove, InputMediaPhoto
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def location(update: Update, context: CallbackContext) -> int:
    user_location = update.message.location

    # write latitude to DB
    insert_update(update.message.from_user.id, 'latitude', user_location.latitude)
    # write longitude to DB
    insert_update(update.message.from_user.id, 'longitude', user_location.longitude)

    logger.info(f'+++++ Location of {update.message.from_user.first_name} {update.message.from_user.last_name}: {user_location.latitude} , {user_location.longitude} +++++')

    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime.',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.PHOTO],
        reply_markup=states.KEYBOARD_MARKUPS[states.PHOTO],
        )
    # TODO: send a picture
    bot_image = f'/ressources/cyberpunk.jpg'
    context.bot.sendMedia(bot_image)

    
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

    update.message.reply_text(
        states.MESSAGES[states.PHOTO],
        reply_markup=states.KEYBOARD_MARKUPS[states.PHOTO],
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO
