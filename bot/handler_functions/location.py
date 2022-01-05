# imports
from telegram import Update
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def location(update: Update) -> int:
    user_location = update.message.location

    # write latitude to DB
    insert_update(update.message.from_user.id, 'latitude', user_location.latitude)

    # write longitude to DB
    insert_update(update.message.from_user.id, 'longitude', user_location.longitude)

    logger.info(f'+++++ Location of {update.message.from_user.first_name} {update.message.from_user.last_name}: {user_location.latitude} , {user_location.longitude} +++++')
    
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        'Here is a picture of me - can you send one of you?'
        '... or just /skip this step.',
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO


# Skips this information and continues on to the next state
def skip_location(update: Update) -> int:

    # mark in db, that no location has been submitted.
    insert_update(update.message.from_user.id, 'latitude', '0')

    # mark in user db, that no location has been submitted.
    insert_update(update.message.from_user.id, 'longitude', '0')
    
    logger.info(f'+++++ No location submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}. +++++')
    
    update.message.reply_text(
        'No matter where you are, coaching will get you to the next level!\n\n'
        'Here is a picture of me - can you send one of you?'
        '... or just /skip this step.',
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO
