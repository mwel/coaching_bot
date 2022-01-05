from telegram import ReplyKeyboardMarkup, Update, message
from telegram.ext import (
    CallbackContext,
)
from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update

# gender copy variables
male = 'Gentleman'
female = 'Lady'
other = 'I am a unicorn.'


# Starts the conversation and asks the user about their gender.
def start(update: Update, context: CallbackContext) -> int:
    
    # if user esists in db: 
        # return user_progress ... and tell the user about it.
    # else... everything below.
    
    
    # ask for user info and write variables to dict
    # user_id
    # context.user_data['user_id'] = update.message.from_user.id # update user dict.
    # first name
    # context.user_data['first_name'] = update.message.from_user.first_name # safe user data into user dictionary like this.
    insert_update(update.message.from_user.id, 'first_name', update.message.from_user.first_name) # saving of user_id not necessary, because it will be saved here anyway.
    # last name
    # context.user_data['last_name'] = update.message.from_user.last_name
    insert_update(update.message.from_user.id, 'last_name', update.message.from_user.last_name)
    # >> safe more initial variables about the user here.
    
    # print status of user dictionary:
    #print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    reply_keyboard = [[female, male, other]]
    update.message.reply_text(
        f'Hi {update.message.from_user.first_name},\n' 'I am a coaching bot by wavehoover. You have taken the first step on you journey to success '
        'by contacting me. I will guide you through the application process for your first coaching session. '
        'It is super easy. Just follow the questions, answer or skip them - that\'s it.'
        '(You can send /cancel at any time, if you are no longer interested in a conversation)\n\n'
        'Ok - let\'s get some basics out of the way: '
        'Would you like to be referred to as lady, gentleman or unicorn?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Lady, Gentleman or are you a unicorn?'
        ),
    )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.GENDER)
    return states.GENDER