import telegram
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
)

# gender copy variables
male = 'Gentleman'
female = 'Lady'
other = 'I am a unicorn.'

GENDER = range(1)

# Starts the conversation and asks the user about their gender.
def start(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [[female, male, other]]

    update.message.reply_text(
        'Hi! I am The Coaching Bot by wavehoover. You have taken the first step in you journey to success '
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