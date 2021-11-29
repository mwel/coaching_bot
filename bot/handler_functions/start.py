from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
)
from conversation_handlers.stage_constants import GENDER

# gender copy variables
male = 'Gentleman'
female = 'Lady'
other = 'I am a unicorn.'


# Starts the conversation and asks the user about their gender.
def start(update: Update, context: CallbackContext) -> int:

    # first name
    first_name = update.message.from_user.first_name

    # write first_name to dict
    context.user_data['first_name'] = first_name # safe user data into user dictionary like this.

    # last name
    last_name = update.message.from_user.last_name
    # safe more initial variables about the user here.
    
    print ('//printing user data: \n' + str(context.user_data))

    reply_keyboard = [[female, male, other]]
    update.message.reply_text(
        f'Hi {context.user_data["first_name"]},\n' 'I am The Coaching Bot by wavehoover. You have taken the first step in you journey to success '
        'by contacting me. As your personal CoachingBot, I will guide you through the onboarding process for '
        'your first coaching session. '
        '(You can send /cancel at any time, if you are no longer interested in a conversation with me '
        'nor your future coach.)\n\n'
        'So - let\'s get started with a simple question: '
        'Would you like to be referred to as a lady or gentleman?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Lady, Gentleman or are you a unicorn?'
        ),
    )

    return GENDER