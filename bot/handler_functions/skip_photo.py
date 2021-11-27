# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from bot.logEnabler import logger;


LOCATION = range(1)


# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User << %s >> did not send a photo.", user.first_name)
    update.message.reply_text(
        'Ok, I\'ll take your word for it and bet you look great! ;)  \n\n'
        'Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, just /skip this step.'
    )

    return LOCATION