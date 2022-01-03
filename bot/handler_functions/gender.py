# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    CallbackContext,
)
from logEnabler import logger;
from conversation_handlers.stage_constants import PHOTO


# Stores the selected gender and asks for a photo.
def gender(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'Gender of {context.user_data["first_name"]} {context.user_data["last_name"]}: {update.message.text}')
    
    # write gender to user dict
    if update.message.text == 'Gentleman':
        context.user_data['gender'] = 'male'
    elif update.message.text == 'Lady':
        context.user_data['gender'] = 'female'
    else:
        context.user_data['gender'] = 'diverse'

    # print status of user dictionary
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    update.message.reply_text(
        f'Alright, {context.user_data["first_name"]}! Now, in order to get to know you better, please send me a photograph of yourself. '
        '(If you don\'t want to or would like to postpone this step, '
        'just send /skip and we will continue to the next step.) ',
        reply_markup=ReplyKeyboardRemove(),
    )

    return PHOTO