# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)

from bot.logEnabler import logger;


# Stores the info about the user and ends the conversation.
def bio(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you so much for signing up! Coaching can change your life and you have just taken the first step in the right direction.')

    return ConversationHandler.END