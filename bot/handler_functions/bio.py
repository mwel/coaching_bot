# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;


# Stores the info about the user and ends the conversation.
def bio(update: Update, context: CallbackContext) -> int:
    logger.info(f'Bio of {context.user_data["first_name"]} {context.user_data["last_name"]}: {update.message.text}')
    # write to user dictionary
    context.user_data['bio'] = update.message.text
    update.message.reply_text(f'Thank you so much for signing up, {context.user_data["first_name"]}! Coaching can change your life and you have just taken the first step in the right direction.')

    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    # TODO: save state to DB
    return ConversationHandler.END