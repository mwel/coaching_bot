# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'User {user.first_name} canceled the conversation.')
    update.message.reply_text(
        f'APPLICATION TERMINATED by {user.first_name}\n\n'
        'You ended the converstation and now have 2 options. Leave OR /start over.'
    )

    return ConversationHandler.END