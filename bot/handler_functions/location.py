# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
import logEnabler;

BIO = range(1)

# Stores the location and asks for some info about the user.
def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location
    logEnabler.logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        'At last, tell me a little bit about yourself, so I can get to know you better.'
    )

    return BIO