""" email handler function. called, when user arrives at email state """

# imports
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update)
from telegram.ext import CallbackContext
from handler_functions.validation import validate_email
from logEnabler import logger;


from handler_functions.states import EMAIL, MESSAGES
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def email(update: Update, context: CallbackContext) -> int:
    
    if validate_email(update.message.text): # if entry is valid, continue.

        logger.info(f'Email address of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

        insert_update(update.message.from_user.id, 'email', update.message.text)

        update.message.reply_text(
            'Ok - I will send you a summary, once we have completed sign up.',
            reply_markup=ReplyKeyboardRemove(),
            )

        update.message.reply_text(
            states.MESSAGES[states.TELEPHONE],
            # reply_markup=states.KEYBOARD_MARKUPS[states.TELEPHONE], # TODO: reactivate once debugged 
            reply_markup=ReplyKeyboardRemove(),
            )
        
        # save state to DB
        insert_update(update.message.from_user.id, 'state', states.TELEPHONE)
        return states.TELEPHONE

    else: # else, tell user and stay in current state until correct entry is provided.
        update.message.reply_text(
        f'Sorry, that\'s not a valid entry. Please try again.',
            reply_markup=ReplyKeyboardRemove(),
        )        

# Skips this information and continues on to the next state
def skip_email(update: Update, context: CallbackContext) -> int:

    logger.info(f'No email address submitted by {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        'Sorry, you cannot skip that one. We need a valid email address for future correspondance. Without an email address, the onboarding cannot be completed.\n\n'
        'Of course you can /cancel at any time. This command will delete all your data from our data base.',
        reply_markup=ReplyKeyboardRemove(),
    )    
