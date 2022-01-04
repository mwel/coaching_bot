from telegram import ReplyKeyboardMarkup, Update, message
from telegram.ext import (
    CallbackContext,
)
from handler_functions import states

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
    context.user_data['user_id'] = update.message.from_user.id # update user dict.
    # first name
    context.user_data['first_name'] = update.message.from_user.first_name # safe user data into user dictionary like this.
    # last name
    context.user_data['last_name'] = update.message.from_user.last_name
    # >> safe more initial variables about the user here.
    
    # print status of user dictionary:
    print ('+++++ User Dictionary +++++ \n' + str(context.user_data) + '\n +++++ +++++ +++++')

    reply_keyboard = [[female, male, other]]
    update.message.reply_text(
        f'Hi {context.user_data["first_name"]},\n' 'I am The Coaching Bot by wavehoover. You have taken the first step in you journey to success '
        'by contacting me. As your personal CoachingBot, I will guide you through the application process for '
        'your first coaching session. '
        '(You can send /cancel at any time, if you are no longer interested in a conversation with me '
        'nor your future coach.)\n\n'
        'Ok - let\'s start with some basics: '
        'Would you like to be referred to as lady, gentleman or unicorn?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Lady, Gentleman or are you a unicorn?'
        ),
    )

    # TODO: save state to DB
    return states.GENDER