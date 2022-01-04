# imports
from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;
from conversation_handlers.stage_constants import BIRTHDATE


# Stores the info about the user and ends the conversation.
def birthdate(update: Update, context: CallbackContext) -> int:

    return BIRTHDATE
