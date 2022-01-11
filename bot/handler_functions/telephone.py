""" telephone handler function. called, when user arrives at telephone state """

# imports
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.validation import validate_telephone



contact_URL = 'https://wavehoover.com/' # adapt accordingly

# Stores the information received and continues on to the next state
def telephone(update: Update, context: CallbackContext) -> int:

    if validate_telephone(update.message.text): # if entry is valid, continue.
    
        logger.info(f'Telephone number of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

        insert_update(update.message.from_user.id, 'telephone', update.message.text)

        update.message.reply_text(
            'Cool, now a coach can call you, if there are any open questions.',
            reply_markup=ReplyKeyboardRemove(),
            )

        update.message.reply_text(
            states.MESSAGES[states.LOCATION],
            reply_markup=states.KEYBOARD_MARKUPS[states.LOCATION],
            )
        
        # save state to DB
        insert_update(update.message.from_user.id, 'state', states.LOCATION)
        return states.LOCATION

    else: # else, tell user and stay in current state until correct entry is provided.
        update.message.reply_text(
        f'Sorry, that\'s not a valid entry. Please try again.',
        reply_markup=states.KEYBOARD_MARKUPS[states.TELEPHONE],
        )


# Skips this information and continues on to the next state
def skip_telephone(update: Update, context: CallbackContext) -> int:
    logger.info(f'No telephone number submitted for {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        f'Ok. No problem. You can still get in touch with your coach via email or the contact form at {contact_URL}',
        reply_markup=ReplyKeyboardRemove(),
    )

    update.message.reply_text(
        states.MESSAGES[states.LOCATION],
        reply_markup=states.KEYBOARD_MARKUPS[states.LOCATION],
        )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION