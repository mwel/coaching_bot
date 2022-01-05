# imports
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext
from logEnabler import logger; 


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update


# Starts the conversation and continues on to the next state
def start(update: Update, context: CallbackContext) -> int:
    
    # if user esists in db: 
        # return user_progress ... and tell the user about it.
    # else... 
    logger.info(f'+++++ NEW USER: {update.message.from_user.first_name} {update.message.from_user.last_name} +++++')

    
    # write user info to db
    insert_update(update.message.from_user.id, 'first_name', update.message.from_user.first_name) # saving of user_id not necessary, because it will be saved here anyway.
    insert_update(update.message.from_user.id, 'last_name', update.message.from_user.last_name)
    # insert_update(update.message.from_user.id, 'phone_number', update.message.from_user.phone_number) # TODO: figure out how to get user's phone number
    # >> safe more initial variables about the user here.
    
    update.message.reply_text(
        f'Hi {update.message.from_user.first_name},\n' 
        'I am a coaching bot by wavehoover. You have taken the first step on your journey to success by contacting me. I will guide you through the application process for your first coaching session. '
        'It\'s super easy. Just follow the questions, answer or skip them - that\'s it.\n\n'
        '[You can send /cancel at any time, if you are no longer interested in a conversation.]\n\n'
        f'Now, {update.message.from_user.first_name} - tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best couching experience possible.'
        )
    
    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIO)
    return states.BIO