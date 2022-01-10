# imports
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def telephone(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text(
        'One of the prep steps for your first face to face session is a quick phone call. '
        'In order for your coach to be able to give you a call, please send me a phone number, we can reach you under:',
        # TODO: reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, input_field_placeholder='+00 000 000 000')
        )
    
    logger.info(f'Telephone number of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    # TODO: data validation phone number

    insert_update(update.message.from_user.id, 'telephone', update.message.text)

    update.message.reply_text(
        'Cool, now a coach can call you, if there are any open questions.\n\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION


# Skips this information and continues on to the next state
def skip_telephone(update: Update, context: CallbackContext) -> int:
    logger.info(f'No telephone number submitted for {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    update.message.reply_text(
        'Ok. No problem. You can still get in touch with your coach via email or the contact form: https://wavehoover.com/ \n\n',
        reply_markup=ReplyKeyboardRemove(),
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION