# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext

from logEnabler import logger;
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
from handler_functions.summary_mail import summary_mail
        

# Stores the photo and asks for a location.
def summary(update: Update, context: CallbackContext) -> int:

    logger.info(f'+++++ User {update.message.from_user.first_name} completed stage 1. +++++')

    first_name = select_db.get_value(update.message.from_user.id, 'first_name')
    last_name = select_db.get_value(update.message.from_user.id, 'last_name')
    gender = select_db.get_value(update.message.from_user.id, 'gender')
    #photo = TODO: get photo into db
    birthdate = select_db.get_value(update.message.from_user.id, 'birthdate')
    email = select_db.get_value(update.message.from_user.id, 'email')
    telephone = select_db.get_value(update.message.from_user.id, 'telephone')
    longitude = select_db.get_value(update.message.from_user.id, 'longitude')
    latitude = select_db.get_value(update.message.from_user.id, 'latitude')
    bio = select_db.get_value(update.message.from_user.id, 'bio')
    state = select_db.get_value(update.message.from_user.id, 'state')
    mail_sent = select_db.get_value(update.message.from_user.id, 'mail_sent')

    summary = f"""Given Name:\t{first_name}
        Last Name:\t{last_name}
        Gender choice:\t{gender}
        Bidthdate:\t{birthdate}
        Email address:\t{email}
        Phone number:\t{telephone}
        Longitude:\t{longitude}
        Latitude:\t{latitude}
        Your story:\t{bio}
        Status:\tSTAGE -1- COMPLETED
        """

    # steps for STAGE 01 COMPLETED
    update.message.reply_text(
        f'Thanks for signing up, {update.message.from_user.first_name}!\n\n' 
        f'SUMMARY for {update.message.from_user.first_name} {update.message.from_user.last_name}:\n\n{summary}',
            reply_markup=ReplyKeyboardRemove(),
    )
    
    update.message.reply_text(
        'What\'s next? \n' 
        'In addition you will receive an email with all your submitted data. From there, you will be able to make an appointment for your first session. Once you\'ve done so, I will get back in touch with you and send you some small tasks for you to prep.\n\n'
        'Until then - have a good one and take care!'
        'Your wavehoover Team',
            reply_markup=ReplyKeyboardRemove(),
    )

    # trigger confirmation email
    summary_mail(first_name, summary, email)
    insert_update(update.message.from_user.id, 'mail_sent', '1')


    # save state to DB
    insert_update(update.message.from_user.id, 'state', 'S1_COMPLETED')
    return ConversationHandler.END

