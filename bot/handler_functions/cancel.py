# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)


from bot.logEnabler import logger;


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'APPLICATION TERMINATED by ' + user.first_name,
        'You ended the converstation and now have 2 options. Leave OR /start over.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END