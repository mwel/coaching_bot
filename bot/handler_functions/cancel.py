""" cancel handler function. called, when user enters /cancel """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;

from handler_functions.database_connector.select_db import get_value
from handler_functions.database_connector.delete_record_db import delete_record
from handler_functions.calendar.calendar_manager import cancel_appointment


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    logger.info(f'XXXXX User {update.message.from_user.first_name} canceled the conversation.')

    # delete record of user upon cancellation of the sign up process
    delete_record(update.message.from_user.id)

    update.message.reply_text(
        f'APPLICATION TERMINATED by {update.message.from_user.first_name}\n\n'
        'You ended the converstation.\n'
        'All your previously submitted data has been deleted.\n\n' 
        'Now you can close this chat\n-OR-\n/start over.',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    return ConversationHandler.END


# delete user record
def delete(update: Update, context: CallbackContext) -> int:
    logger.info(f'XXXXX User {update.message.from_user.first_name} deleted own user record.')

    # delete record of user upon cancellation of the sign up process
    delete_record(update.message.from_user.id)

    update.message.reply_text(
        '- - - SUCCESS - - -\n'
        'All your previously submitted data has been deleted.\n\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    return ConversationHandler.END


# delete user record
def cancel_appointment(update: Update, context: CallbackContext) -> int:
    logger.info(f'XXXXX User {update.message.from_user.first_name} cancelled appointment.')

    # tell google Calendar API to cancel the appointment with this user
    user_id = update.message.from_user.id
    slot_start = get_value(user_id, 'appointment')
    event = get_value(user_id, 'event')
    cancel_appointment(user_id=user_id, slot_start=slot_start, event=event)

    update.message.reply_text(
        '- - - SUCCESS - - -\n'
        'All your previously submitted data has been deleted.\n\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    return ConversationHandler.END