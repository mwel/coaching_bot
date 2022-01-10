# imports
from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db


from handler_functions.database_connector.create_db import create_db


# Starts the conversation and continues on to the next state
def start(update: Update, context: CallbackContext) -> int:

    # CREATE DB, IF NOT EXISTS
    create_db()

    user_exists = select_db.user_search(update.message.from_user.id)  # maybe also check, whether there is a db value saved in 'state'
    if user_exists:
        # get user's state from db
        state = int(select_db.get_value(update.message.from_user.id, 'state'))

        update.message.reply_text(
            f'Welcome back {update.message.from_user.first_name},\n'
            'Let\'s continue where we left off...\n\n',
            # '(In case you would like to start over, just /cancel and /start again.)',
            reply_markup=ReplyKeyboardRemove(),
            )

        if state == states.COMPLETED:  # stage 1 was apparently already completed for this user in the past.
            reply_keyboard = [['/cancel'],['/summary']]
            update.message.reply_text(
           'Ah! I see, you have already completed stage 1 of the sign up.\nYou now have 2 options:\n'
           'Go to your email account and check, whether you have received our summary or just go back to your /summary here\n'
           '- OR -\ndelete all your data you have previously entered via /cancel and /start over.',
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='STAGE -1- COMPLETE'
                )
            )
            return ConversationHandler.END

        # call next function for user
        return state

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
        '[You can send /cancel at any time, if you are no longer interested in a conversation.]\n\n',
        reply_markup=ReplyKeyboardRemove(),
        )

    # save state to DB
    insert_update(update.message.from_user.id, 'state', states.BIO)
    return states.BIO
