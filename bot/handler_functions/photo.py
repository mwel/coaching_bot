# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from conversation_handlers.stage_constants import LOCATION


# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(user.first_name+'_photo.jpg') #add date to photo
    context.user_data['user_photo'] = photo_file
    logger.info(f'Photo of {context.user_data["first_name"]} {context.user_data["last_name"]}: {user.first_name+"_photo.jpg"}')

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    update.message.reply_text(
        'Gorgeous! Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, you can /skip this step.'
    )

    return LOCATION


# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'User {context.user_data["first_name"]} {context.user_data["last_name"]} did not submit a photo.')

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')
    
    update.message.reply_text(
        'Ok, I\'ll take your word for it and bet you look great! ;)  \n\n'
        'Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, just /skip this step.'
    )

    return LOCATION