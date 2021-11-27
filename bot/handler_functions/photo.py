# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from bot.logEnabler import logger;


LOCATION = range(1)


# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(user.first_name+'_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, user.first_name+'_photo.jpg')
    update.message.reply_text(
        'Gorgeous! Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, you can /skip this step.'
    )

    return LOCATION