# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;
from handler_functions.database_connector.insert_value_db import insert_update



# Stores the info about the user and ends the conversation.
def bio(update: Update, context: CallbackContext) -> int:
    logger.info(f'Bio of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')
    # write to user dictionary
    # context.user_data['bio'] = update.message.text
    # write bio to DB
    insert_update(update.message.from_user.id, 'bio', update.message.text)

    # copy for STAGE 01 COMPLETED
    update.message.reply_text(f'Thanks for signing up, {update.message.from_user.first_name}! What\'s next? \n\n You will receive an email with all your submitted data. From there, you will be able to make an appointment for your first session. Once you\'ve done so, I will get back in touch with you and send you some small tasks for you to prep. \n\nUntil then - have a good one and take care!')

    # print status of user dictionary:
    # print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    # save state to DB
    insert_update(update.message.from_user.id, 'state', 'COMPLETED')
    return ConversationHandler.END