""" Summary feature. Collects all data on a user from the data base, 
packages it into one message and displays it to the user upon completion 
of sign up. Also triggers email and appointment delivery."""

# imports
from select import select
from telegram import ReplyKeyboardRemove, Update, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector.select_db import get_value, user_search
from handler_functions.confirmation_mail import confirmation_mail
# from handler_functions.calendar.generate_ics import generate_ics
# from handler_functions.calendar.send_invitation import send_invitation
# from handler_functions.appointment import appointment
from handler_functions.calendar.calendar_manager import find_slots


# Stores the photo and asks for a location.
def summary(update: Update, context: CallbackContext) -> int:
    
    user_id = update.message.from_user.id    

    logger.info(f'+++++ User {update.message.from_user.first_name} COMPLETED SIGN UP. +++++')

    first_name = get_value(user_id, 'first_name')
    last_name = get_value(user_id, 'last_name')
    gender = get_value(user_id, 'gender')
    birthdate = get_value(user_id, 'birthdate')
    email = get_value(user_id, 'email')
    telephone = get_value(user_id, 'telephone')
    # longitude = get_value(user_id, 'longitude')
    # latitude = get_value(user_id, 'latitude')
    # bio = get_value(user_id, 'bio')
    # state = get_value(user_id, 'state')
    # mail_sent = get_value(user_id, 'mail_sent')

    summary = f"""
        Given Name:\t\t{first_name}
        Last Name:\t\t{last_name}
        Gender choice:\t\t{gender}
        Birthdate:\t\t\t{birthdate}
        Email address:\t\t{email}
        Phone number:\t{telephone}
        """
        # Longitude:\t\t{longitude}
        # Latitude:\t\t\t{latitude}
        # Your story:\t\t{bio}
        # Sign Up:\t\t\t{state}


    # confirmation message
    update.message.reply_text(
        f'Thanks for signing up, {update.message.from_user.first_name}!\n\n'
        f'SUMMARY for {update.message.from_user.first_name} {update.message.from_user.last_name}:\n\n{summary}',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # check, if the user already made an appointment. 
    appointment_made = get_value(user_id, 'appointment')
    
    # If no, make one. Else, inform.
    if appointment_made == 'None':
        
        update.message.reply_text(
            'Ok. We will look for 3 appointment options you can choose from for your phone call. \n\n'
            '... SEARCHING ...',
            reply_markup=ReplyKeyboardRemove(),
        )

        free_slots = find_slots()

        slot1 = str(free_slots[0])
        slot2 = str(free_slots[1])
        slot3 = str(free_slots[2])

        # next step message
        update.message.reply_text(
            states.MESSAGES[states.APPOINTMENT],
            reply_markup=ReplyKeyboardMarkup(
                [[slot1], [slot2], [slot3]], ['/skip'], 
                one_time_keyboard=True, 
                input_field_placeholder='Choose your slot...'
                )
            )

    else:
        update.message.reply_text(
            f'Cool. You already have an appointment: {appointment_made} \n\n'
            'In case you would like to cancel, you can do so via your calendar app.\n\n'
            'Otherwise, we are looking forward to our call.',
            reply_markup=ReplyKeyboardRemove(),
        )

        return ConversationHandler.END


    # trigger confirmation email
    confirmation_mail(first_name, summary, email)
    insert_update(user_id, 'mail_sent', '1')

    # save state to DB
    insert_update(user_id, 'state', states.APPOINTMENT)
    return states.APPOINTMENT


    
