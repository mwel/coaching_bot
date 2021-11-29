# imports
from telegram import Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from conversation_handlers.stage_constants import BIO


# Stores the location and asks for some info about the user.
def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location

    # write location to user dict
    context.user_data['latitude'] = user_location.latitude
    context.user_data['longitude'] = user_location.longitude

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    logger.info(
        "Location of %s %s: %f / %f", context.user_data['first_name'], context.user_data['last_name'], user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        'Now - tell me a little bit about yourself, so I can get to know you better.'
    )

    return BIO


# Skips the location and asks for info about the user.
def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user

    # mark in user dict, that no location has been supplied.
    context.user_data['latitude'] = 'N/A'
    context.user_data['longitude'] = 'N/A'

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')
    
    logger.info("User %s %s did not submit a location.", context.user_data['first_name'], context.user_data['last_name'])
    update.message.reply_text(
        'No matter where you are, coaching will get you to the next level!  \n\n'
        'Now, %s - tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best consulting service possible.'
    ), context.user_data['first_name']

    return BIO