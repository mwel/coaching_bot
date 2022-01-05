# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(user.first_name+'_photo.jpg') #add date to photo

    # convert to binary
    with open(photo_file, 'rb') as file:
        binary_photo_file = file.read()
    

    context.user_data['user_photo'] = photo_file
    insert_update(update.message.from_user.id, 'photo', photo_file) # ERROR: unsupported type
    logger.info(f'Photo of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.from_user.first_name+"_photo.jpg"}')

    # print status of user dictionary:
    # print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    update.message.reply_text(
        'Great picture!\n\n Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, you can always /skip this step.'
    )
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION

# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} did not update.message.from_user.first_namephoto.')
    insert_update(update.message.from_user.id, 'photo', 'NULL')

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')
    
    update.message.reply_text(
        'Ok, I\'ll take your word for it and bet you look great! ;)  \n\n'
        'Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, just /skip this step.'
    )
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION