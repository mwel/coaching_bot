# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from conversation_handlers.stage_constants import BIO


# Stores the location and asks for some info about the user.
def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        'At last, tell me a little bit about yourself, so I can get to know you better.'
    )

    return BIO


# Skips the location and asks for info about the user.
def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'Ok, you seem a bit paranoid, but then again - you can never be too careful!  \n\n'
        'Now, at last, tell me a little bit about yourself - otherwise this really doesn\'t make any sense. ;).'
    )

    return BIO