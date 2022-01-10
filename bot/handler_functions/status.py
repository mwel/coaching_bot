""" status handler function. called, when user enters /status """

# imports
from telegram import ReplyKeyboardRemove, Update, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler, CallbackContext

from logEnabler import logger;


from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
from handler_functions import states

# Stores the photo and asks for a location.
def status(update: Update, context: CallbackContext) -> int:

    if select_db.user_search(update.message.from_user.id):
        state = select_db.get_value(update.message.from_user.id, 'state')

        # return message, if user had been found in db
        update.message.reply_text(
            f'You have completed {state} out of {states.MAX_STATES} steps of the sign-up!\n\n',
                reply_markup=ReplyKeyboardRemove(),
        )
        return ConversationHandler.END

    reply_keyboard = [['/start'],['/help']]
    # return message, if user could not be found in db
    update.message.reply_text(
        'Hi there - we couldn\'t find you in our data base. Looks like you\'ve either never been here before or deleted all your data.'
        'You can /start over at any time or look at the help to get orientated.',
        reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True
        )
    )
    return ConversationHandler.END
