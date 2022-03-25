""" location handler function. called, when user arrives at location state """

# imports
from telegram import Update, ReplyKeyboardRemove, Bot
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from pathlib import Path
import os


# build the path to the photo to be sent to the user
directory = os.path.join(str(Path(__file__).parent.parent), 'ressources', 'cyberpunk.jpg')
# print(f'>>>>>>>>>>>>> Photo Directory: {directory}')
# directory = 'https://github.com/mwel/coaching_bot/blob/main/bot/ressources/cyberpunk.jpg'


# Stores the information received and continues on to the next state
def location(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id
    chat_id=update.effective_user.id
    user_location = update.message.location
    
    logger.info(f'+++++ Location of user {user_id}: {user_location.latitude} , {user_location.longitude} +++++')

    # write latitude to DB
    insert_update(user_id, 'latitude', user_location.latitude)
    # write longitude to DB
    insert_update(user_id, 'longitude', user_location.longitude)


    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime.',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.PHOTO],
        reply_markup=states.KEYBOARD_MARKUPS[states.PHOTO],
        )

    # send userpic to the user
    context.bot.send_photo(chat_id=chat_id, photo=open(directory, 'rb'))

    
    # save state to DB
    insert_update(user_id, 'state', states.PHOTO)
    return states.PHOTO


# Skips this information and continues on to the next state
def skip_location(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id
    chat_id = update.message.chat_id

    logger.info(f'00000 No location submitted by {user_id}. 00000')

    update.message.reply_text(
        'No matter where you are, coaching will get you to the next level!',
        reply_markup=ReplyKeyboardRemove(),
        )

    update.message.reply_text(
        states.MESSAGES[states.PHOTO],
        reply_markup=states.KEYBOARD_MARKUPS[states.PHOTO],
        )

    # send userpic to the user
    context.bot.send_photo(chat_id=chat_id, photo=open(directory, 'rb'))


    # save state to DB
    insert_update(user_id, 'state', states.PHOTO)
    return states.PHOTO
