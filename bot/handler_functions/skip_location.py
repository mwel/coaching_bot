# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
import logEnabler;

BIO = range(1)

# Skips the location and asks for info about the user.
def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logEnabler.logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'Ok, you seem a bit paranoid, but then again - you can never be too careful!  \n\n'
        'Now, at last, tell me a little bit about yourself - otherwise this really doesn\'t make any sense. ;).'
    )

    return BIO