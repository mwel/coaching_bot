# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;
import states


# Stores the info about the user and ends the conversation.
def birthdate(update: Update, context: CallbackContext) -> int:

    return states.BIRTHDATE
