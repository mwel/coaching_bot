""" photo handler function. called, when user arrives at photo state """

# imports
from telegram import ReplyKeyboardRemove, ReplyKeyboardMarkup, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from pathlib import Path
import os


# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id

    photo_file = update.message.photo[-1].get_file()
    directory = str(Path(__file__).parent.parent)
    photo_file.download(os.path.join(directory, 'static', 'user_pictures', str(user_id) + '.jpg'))

    # log info
    logger.info(f'+++++ Photo of user {user_id}: {update.message.from_user.first_name+"_photo.jpg"} +++++')

    update.message.reply_text(
        'Great picture!',
        reply_markup=ReplyKeyboardRemove(),
        )
    
    update.message.reply_text(
        states.MESSAGES[states.SUMMARY],
        reply_markup=states.KEYBOARD_MARKUPS[states.SUMMARY],
        )

    # save state to DB
    insert_update(user_id, 'state', states.SUMMARY)
    return states.SUMMARY


# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id
    
    logger.info(f'00000 User {user_id} did not submit a photo. 00000')
    
    update.message.reply_text(
        'No problem. :) You can send me a picture later, if you like.',
        reply_markup=ReplyKeyboardRemove(),
        )
        
    update.message.reply_text(
        states.MESSAGES[states.SUMMARY],
        reply_markup=states.KEYBOARD_MARKUPS[states.SUMMARY],
        )

    # save state to DB
    insert_update(user_id, 'state', states.SUMMARY)
    return states.SUMMARY