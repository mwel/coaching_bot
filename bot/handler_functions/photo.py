""" photo handler function. called, when user arrives at photo state """

# imports
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


reply_keyboard = [['COMPLETE SIGN UP'],['/cancel']]

# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(update.message.from_user.first_name+'_photo.jpg') # TODO: add date to photo

    # write to user dict
    context.user_data['user_photo'] = photo_file

    # TODO: save image in db as BLOB
    # convert to binary
    # with open(photo_file, 'rb') as file:
    #     binary_photo_file = file.read()
    
    # write pic to db
    # insert_update(update.message.from_user.id, 'photo', binary_photo_file) # ERROR: unsupported type
    # log info
    logger.info(f'Photo of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.from_user.first_name+"_photo.jpg"}')

    update.message.reply_text(
        'Great picture!\n\n'
        'You are now at the end of stage 1. Would you like to complete your sign up for personal coaching or rather /cancel?',
        reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, input_field_placeholder='COMPLETE SIGN UP'
        )
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.SUMMARY)
    return states.SUMMARY


# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} did not update.message.from_user.first_namephoto.')
    insert_update(update.message.from_user.id, 'photo', 'NULL')
    
    update.message.reply_text(
        'Great picture!\n\n'
        'You are now at the end of stage 1. Would you like to complete your sign up for personal coaching or rather /cancel?',
        reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True, input_field_placeholder='COMPLETE SIGN UP'
        )
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.SUMMARY)
    return states.SUMMARY