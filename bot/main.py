#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# imports
import telegram
from constants.API_constant import API_KEY
from utils.persistenceTest import PersistenceTest
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from handler_functions.start import start
from handler_functions.bio import bio
from handler_functions.gender import gender
from handler_functions.photo import photo, skip_photo
from handler_functions.location import location, skip_location
from handler_functions.cancel import cancel
from handler_functions import states


# Hand over API_TOKEN to the bot
bot = telegram.Bot(token=API_KEY)


print(bot.get_me())
{"first_name": "The Coaching Bot", "username": "TheCoachingBot"}


# Runs the bot.
def main() -> None:
    #create dummy persistance class until I know how it works.
    persistence = PersistenceTest(store_user_data=True, store_chat_data=True, store_bot_data=True, store_callback_data=True) #why user data didn't generate?

    # Creates the updater and passes the API_TOKEN to it.
    updater = Updater(API_KEY, persistence=persistence)

    # Gets the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # this is the STATE MACHINE
    # Adds conversation handler with the states GENDER, PHOTO, LOCATION and BIO for stage 1 of the sign up
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            states.GENDER:      [MessageHandler(Filters.regex('^(Gentleman|Lady|I am a unicorn.)$'), gender)],
            states.PHOTO:       [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            states.LOCATION:    [MessageHandler(Filters.location, location), CommandHandler('skip', skip_location)],
            states.BIO:         [MessageHandler(Filters.text & ~Filters.command, bio)],
            # more states here...
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler) #calling Handler from separate class
    # more Handlers here...

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
