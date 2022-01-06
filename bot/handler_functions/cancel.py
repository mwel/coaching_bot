# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;


from handler_functions.database_connector.delete_record_db import delete_record


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info(f'User {user.first_name} canceled the conversation.')

    # delete record of user upon cancellation of the sign up process
    delete_record(update.message.from_user.id)

    update.message.reply_text(
        f'APPLICATION TERMINATED by {user.first_name}\n\n'
        'You ended the converstation.'
        'All your previously submitted data has been deleted.\n\n' 
        'Now you can close this chat -OR- /start over.',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    return ConversationHandler.END