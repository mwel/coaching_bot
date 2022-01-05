# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the info about the user and ends the conversation.
def birthdate(update: Update, context: CallbackContext) -> int:

    insert_update(update.message.from_user.id, 'state', states.BIRTHDATE)
    return states.BIRTHDATE
