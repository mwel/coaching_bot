""" Summary feature. Collects all data on a user from the data base, packages it into one message and displays it to the user upon completion of sign up."""

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext

from logEnabler import logger;
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
from handler_functions.summary_mail import summary_mail


# Stores the photo and asks for a location.
def summary(update: Update, context: CallbackContext) -> int:

    logger.info(f'+++++ User {update.message.from_user.first_name} COMPLETED SIGN UP. +++++')

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

    # if all questions of the bot have been ansered of skipped, send COMPLETE tag to user. Else - send status.
    if state == states.COMPLETED:
        state = 'COMPLETE'

    summary = f"""Given Name:\t\t{first_name}
        Last Name:\t\t{last_name}
        Gender choice:\t\t{gender}
        Bidthdate:\t\t\t{birthdate}
        Email address:\t\t{email}
        Phone number:\t{telephone}
        Longitude:\t\t{longitude}
        Latitude:\t\t\t{latitude}
        Your story:\t\t{bio}
        Sign Up:\t\t\t{state}
        """

    # confirmation message
    update.message.reply_text(
        f'Thanks for signing up, {update.message.from_user.first_name}!\n\n'
        f'SUMMARY for {update.message.from_user.first_name} {update.message.from_user.last_name}:\n\n{summary}',
        reply_markup=ReplyKeyboardRemove(),
    )
    # next steps message
    update.message.reply_text(
        states.MESSAGES[states.COMPLETED],
        reply_markup=ReplyKeyboardRemove(),
    )

    # trigger confirmation email
    summary_mail(first_name, summary, email)
    insert_update(update.message.from_user.id, 'mail_sent', '1')


    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.COMPLETED)
    return ConversationHandler.END
