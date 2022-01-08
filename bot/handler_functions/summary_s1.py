# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext

from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
        

# Stores the photo and asks for a location.
def summary(update: Update, context: CallbackContext) -> int:

    logger.info(f'+++++ User {update.message.from_user.first_name} completed stage 1. +++++')

    summary = f"""Given Name = {select_db.get_value(update.message.from_user.id, 'first_name')}
        Last Name: {select_db.get_value(update.message.from_user.id, 'last_name')}
        Gender choice: {select_db.get_value(update.message.from_user.id, 'gender')}
        Bidthdate: {select_db.get_value(update.message.from_user.id, 'birthdate')}
        Email address: {select_db.get_value(update.message.from_user.id, 'email')}
        Phone number: {select_db.get_value(update.message.from_user.id, 'telephone')}
        Longitude: {select_db.get_value(update.message.from_user.id, 'longitude')}
        Latitude: {select_db.get_value(update.message.from_user.id, 'latitude')}
        Your story: {select_db.get_value(update.message.from_user.id, 'bio')}
        Status: Stage -1- completed'
        """

    # steps for STAGE 01 COMPLETED
    update.message.reply_text(
        f'Thanks for signing up, {update.message.from_user.first_name}!\n\n' 
        f'SUMMARY for {update.message.from_user.first_name} {update.message.from_user.last_name}:\n\n{summary}'
        'What\'s next? \n' 
        'In addition you will receive an email with all your submitted data. From there, you will be able to make an appointment for your first session. Once you\'ve done so, I will get back in touch with you and send you some small tasks for you to prep.\n\n'
        'Until then - have a good one and take care!'
        'Your wavehoover Team',
            reply_markup=ReplyKeyboardRemove(),
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', 'S1_COMPLETED')
    return ConversationHandler.END