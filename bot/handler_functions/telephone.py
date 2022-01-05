# imports
from telegram import Update
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Stores the information received and continues on to the next state
def telephone(update: Update) -> int:
    logger.info(f'Telephone number of {update.message.from_user.first_name} {update.message.from_user.last_name}: {update.message.text}')

    insert_update(update.message.from_user.id, 'telephone', update.message.text)

    update.message.reply_text(
        'Cool, now a coach can call you, if there are any open questions.\n\n'
        f'Alright, {update.message.from_user.first_name} - let\'s continue... '
        'I\'m from Switzerland. It\'s really nice here! Where are you from?\n\n'
        '- > Tip: Use Telegram\'s built in function to share your location with me.\n\n'
        'Or, if you prefer not to, just /skip this step.',
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION


# Skips this information and continues on to the next state
def skip_telephone(update: Update) -> int:
    logger.info(f'No telephone number submitted for {update.message.from_user.first_name} {update.message.from_user.last_name}.')

    # insert_update(update.message.from_user.id, 'telephone', '0')

    update.message.reply_text(
        'Ok. No problem. You can still get in touch with your coach via email or the contact form: https://wavehoover.com/ \n\n'
        f'Alright, {update.message.from_user.first_name} - let\'s continue... '
        'I\'m from Switzerland. It\'s really nice here! Where are you from?\n\n'
        '- > Tip: Use Telegram\'s built in function to share your location with me.\n\n'
        'Or, if you prefer not to, just /skip this step.',
    )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.LOCATION)
    return states.LOCATION