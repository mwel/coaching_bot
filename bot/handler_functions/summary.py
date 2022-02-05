""" Summary feature. Collects all data on a user from the data base, 
packages it into one message and displays it to the user upon completion 
of sign up. Also triggers email and appointment delivery."""

# imports
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector.select_db import get_value
from handler_functions.confirmation_mail import confirmation_mail
from handler_functions.calendar.generate_ics import generate_ics
from handler_functions.calendar.send_invitation import send_invitation
from handler_functions.make_appointment import make_appointment


# Stores the photo and asks for a location.
def summary(update: Update, context: CallbackContext) -> int:

    logger.info(f'+++++ User {update.message.from_user.first_name} COMPLETED SIGN UP. +++++')

    first_name = get_value(update.message.from_user.id, 'first_name')
    last_name = get_value(update.message.from_user.id, 'last_name')
    gender = get_value(update.message.from_user.id, 'gender')
    #photo = TODO: get photo into db
    birthdate = get_value(update.message.from_user.id, 'birthdate')
    email = get_value(update.message.from_user.id, 'email')
    telephone = get_value(update.message.from_user.id, 'telephone')
    longitude = get_value(update.message.from_user.id, 'longitude')
    latitude = get_value(update.message.from_user.id, 'latitude')
    bio = get_value(update.message.from_user.id, 'bio')
    state = get_value(update.message.from_user.id, 'state')
    mail_sent = get_value(update.message.from_user.id, 'mail_sent')

    # if all questions of the bot have been ansered of skipped, send COMPLETE tag to user. Else - send status.
    if state == states.COMPLETED:
        state = 'COMPLETE'

    summary = f"""
        Given Name:\t\t{first_name}
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
    # next step message
    update.message.reply_text(
        states.MESSAGES[states.APPOINTMENT],
        reply_markup=states.KEYBOARD_MARKUPS[states.APPOINTMENT],
        )

    # trigger confirmation email
    confirmation_mail(first_name, summary, email)
    insert_update(update.message.from_user.id, 'mail_sent', '1')

    # trigger calendar invitation TODO: make calendar invited dynamic
    # coach_name = 'Max'
    # coach_email = 'max@wavehoover.com'
    # ics= generate_ics(
    #     coachee_name=first_name, 
    #     coachee_email=email, 
    #     coachee_phone_number=telephone,
    #     coach_name=coach_name, 
    #     coach_email=coach_email, 
    #     year = 2022,
    #     month = 1,
    #     day =1,
    #     start_hour=9,
    #     start_minute=0, 
    #     end_hour=10,
    #     end_minute=0, 
    #     )
    

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.APPOINTMENT)
    return states.APPOINTMENT
