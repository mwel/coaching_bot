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
        'APPLICATION TERMINATED by ' + user.first_name,
        'You ended the converstation and now have 2 options. Leave OR /start over.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END