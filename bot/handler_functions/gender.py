# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the selected gender and asks for a photo.
def gender(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'Gender of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')
    
    # write gender to user dict
    if update.message.text == 'Gentleman':
        # context.user_data['gender'] = 'male'
        insert_update(update.message.from_user.id, 'gender', 'male')

    elif update.message.text == 'Lady':
        # context.user_data['gender'] = 'female'
        insert_update(update.message.from_user.id, 'gender', 'female')
    else:
        # context.user_data['gender'] = 'diverse'
        insert_update(update.message.from_user.id, 'gender', 'diverse') 


    # print status of user dictionary
    # print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    update.message.reply_text(
        f'Alright, {update.message.from_user.first_name}! Now, in order to get to know you better, please send me a photograph of yourself. '
        '(If you don\'t want to or would like to postpone this step, '
        'just send /skip and we will continue to the next step.) ',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.PHOTO)
    return states.PHOTO