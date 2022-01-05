# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the location and asks for some info about the user.
def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location

    # write latitude to user dict
    # context.user_data['latitude'] = user_location.latitude
    # write latitude to DB
    insert_update(update.message.from_user.id, 'latitude', user_location.latitude)

    # write longitude to user dict
    # context.user_data['longitude'] = user_location.longitude
    # write longitude to DB
    insert_update(update.message.from_user.id, 'longitude', user_location.longitude)

    # print status of user dictionary:
    # print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    logger.info(
        f'Location of {update.message.from_user.first_name} {update.message.from_user.last_name}: {user_location.latitude} , {user_location.longitude}'
    )
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        f'Now, {update.message.from_user.first_name} - tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best couching experience possible.')
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIO)
    return states.BIO


# Skips the location and asks for info about the user.
def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user

    # mark in user dict, that no location has been submitted.
    # context.user_data['latitude'] = 'N/A'
    # mark in db, that no location has been submitted.
    insert_update(update.message.from_user.id, 'latitude', '0')

    # mark in user dict, that no location has been submitted.
    # context.user_data['longitude'] = 'N/A'
    # mark in user db, that no location has been submitted.
    insert_update(update.message.from_user.id, 'longitude', '0')

    # print status of user dictionary:
    # print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')
    
    logger.info(f'User {update.message.from_user.first_name} {update.message.from_user.last_name} did not submit a location.')
    update.message.reply_text(
        'No matter where you are, coaching will get you to the next level!  \n\n'
        f'Now, {update.message.from_user.first_name} - tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best consulting service possible.')
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIO)
    return states.BIO
