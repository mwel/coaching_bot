""" cancel handler function. called, when user enters /cancel """

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    ConversationHandler,
    CallbackContext,
)
from logEnabler import logger;

from handler_functions.database_connector.select_db import get_value
from handler_functions.database_connector.delete_record_db import delete_record, delete_value
from handler_functions.calendar.calendar_manager import cancel_appointment


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    
    try:
        logger.info(f'----- User {update.message.from_user.first_name} canceled the conversation. -----')

        # delete record of user upon cancellation of the sign up process
        delete_record(update.message.from_user.id)

        update.message.reply_text(
            '- - - SUCCESS - - -\n'
            f'APPLICATION TERMINATED by {update.message.from_user.first_name}\n\n'
            'All your previously submitted data has been deleted.\n\n' 
            'Now you can close this chat\n-OR-\n/start over.',
            reply_markup=ReplyKeyboardRemove(),
        )
    
    except Exception as exc:
        logger.info(exc)
        logger.info(f'----- ERROR: User {update.message.from_user.first_name} tried to cancel the bot, but was not able to.')
        update.message.reply_text(
            '- - - ERROR - - -\n'
            'Sorry - something went wrong. Maybe you need to /start the bot first?',
            reply_markup=ReplyKeyboardRemove(),
        )

    return ConversationHandler.END


# delete user record
def delete(update: Update, context: CallbackContext) -> int:
    
    try:
        logger.info(f'----- User {update.message.from_user.first_name} deleted own user record. -----')

        # delete record of user upon cancellation of the sign up process
        delete_record(update.message.from_user.id)

        update.message.reply_text(
            '- - - SUCCESS - - -\n'
            'All your previously submitted data has been deleted.\n\n',
            reply_markup=ReplyKeyboardRemove(),
        )

    except Exception as exc:
        logger.info(exc)
        logger.info(f'----- ERROR: User {update.message.from_user.first_name} tried to delete his data, but was not able to.')
        update.message.reply_text(
            '- - - ERROR - - -\n'
            'Sorry - something went wrong. Maybe you have not entered any data yet? To check, enter /start OR /cancel.',
            reply_markup=ReplyKeyboardRemove(),
        )

    return ConversationHandler.END



# cancel appointment and remove it from calendars
def cancel_appointment(update: Update, context: CallbackContext) -> int:

    try:

        # tell google Calendar API to cancel the appointment with this user
        user_id = update.message.from_user.id
        slot_start = get_value(user_id, 'appointment')
        event = get_value(user_id, 'event_id')
        cancel_appointment(user_id, slot_start)

        # remove values from db
        delete_value(user_id, 'appointment')
        delete_value(user_id, 'event_id')

        logger.info(f'----- User {update.message.from_user.first_name} cancelled appointment.')
        update.message.reply_text(
            '- - - SUCCESS - - -\n'
            'Your appointment has been canceled.\n\n You can make a new appointment by entering /summary.',
            reply_markup=ReplyKeyboardRemove(),
        )
    
    except Exception as exc:
        logger.info(exc)
        logger.info(f'----- ERROR: User {update.message.from_user.first_name} tried to cancel, but was not able to.')
        update.message.reply_text(
            '- - - ERROR - - -\n'
            'Sorry - something went wrong. Please try to cancel your appointment via your calendar app or just give us a quick call. ',
            reply_markup=ReplyKeyboardRemove(),
        )

    return ConversationHandler.END