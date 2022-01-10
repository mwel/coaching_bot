# imports
from telegram import (ReplyKeyboardMarkup, KeyboardButton, Update)
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# TODO: Keyboard for email
reply_keyboard = [] # TODO: implement normal or mail keyboard

# replymarkup_variable for next state
reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,
            input_field_placeholder='mybestmail@me.com'
            )


# Stores the information received and continues on to the next state
def email(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        'Now, send me your email address, so I can send you your summary of submitted data upon completion.\n\n',
        reply_markup=reply_markup,
        # TODO: reply_markup=custom_markup,
    )
    
    logger.info(f'Email address of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    # TODO: data validation email address

    insert_update(update.message.from_user.id, 'email', update.message.text)

    update.message.reply_text(
        'Ok - I will send you a summary, once we have completed the sign up. \n\n'
        'One of the prep steps for your first face to face session is a quick phone call. '
        'In order for your coach to be able to give you a call, please send me a phone number, we can reach you under:',
        # TODO: reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder='+00 000 000 000')
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.TELEPHONE)
    return states.TELEPHONE


# Skips this information and continues on to the next state
def skip_email(update: Update, context: CallbackContext) -> int:
    logger.info(f'No email address submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    reply_keyboard = [
        ['/email'], # TODO: implement entry point for /email in main.py
        ['/cancel']],

    update.message.reply_text(
        'Sorry, without an email address, the onboarding cannot be finished. Please enter one or /cancel\n\n'
        'WARNING: If you cancel, all your previously submitted data will be deleted and you have to start over.',
        # TODO: reply_markup=ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder='mybest@address.com')
    )
    # Looping back to state: EMAIL (we do not want to save anything to the db as we want to user to submit an email) 
    return states.EMAIL
    
