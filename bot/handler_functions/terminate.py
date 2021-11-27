# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)

import logEnabler;

# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logEnabler.logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'APPLICATION TERMINATED by ' + user.first_name,
        'You ended the converstation and now have 2 options. Leave OR /start over.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END