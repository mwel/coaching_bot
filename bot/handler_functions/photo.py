# imports
from telegram import (ReplyKeyboardRemove, Update)
from telegram.ext import CallbackContext

from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(update.message.from_user.first_name+'_photo.jpg') #add date to photo

    # convert to binary
    # with open(photo_file, 'rb') as file:
    #     binary_photo_file = file.read()
    
    # write to user dict
    context.user_data['user_photo'] = photo_file
    # write pic top db
    # insert_update(update.message.from_user.id, 'photo', binary_photo_file) # ERROR: unsupported type
    # log info
    logger.info(f'Photo of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.from_user.first_name+"_photo.jpg"}')

    update.message.reply_text(
        'Great picture!',
        reply_markup=ReplyKeyboardRemove()
    )

    # copy for STAGE 01 COMPLETED
    update.message.reply_text(f'Thanks for signing up, {update.message.from_user.first_name}! What\'s next? \n\n You will receive an email with all your submitted data. From there, you will be able to make an appointment for your first session. Once you\'ve done so, I will get back in touch with you and send you some small tasks for you to prep. \n\nUntil then - have a good one and take care!')

    # save state to DB
    insert_update(update.message.from_user.id, 'state', 'S1_COMPLETED')
    return 'S1_COMPLETED'

# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} did not update.message.from_user.first_namephoto.')
    insert_update(update.message.from_user.id, 'photo', 'NULL')
    
    update.message.reply_text(
        'Ok, I\'ll take your word for it and bet you look great! ;)  \n\n',
         reply_markup=ReplyKeyboardRemove()
    )

    # copy for STAGE 01 COMPLETED
    update.message.reply_text(f'Thanks for signing up, {update.message.from_user.first_name}! What\'s next? \n\n You will receive an email with all your submitted data. From there, you will be able to make an appointment for your first session. Once you\'ve done so, I will get back in touch with you and send you some small tasks for you to prep. \n\nUntil then - have a good one and take care!')

    # save state to DB
    insert_update(update.message.from_user.id, 'state', 'S1_COMPLETED')
    return 'S1_COMPLETED'