#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

# connect and launch the bot by entering this in your webbrowser: https://t.me/thecoachingbot?start=start

""" -- main -- of the coaching Bot by wavehoover """

# imports
import telegram
from constants.API_constant import API_KEY
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
from handler_functions.birthdate import birthdate, skip_birthdate
from handler_functions.email import email, skip_email
from handler_functions.telephone import telephone, skip_telephone
from handler_functions.location import location, skip_location
from handler_functions.photo import photo, skip_photo
from handler_functions.summary_s1 import summary
from handler_functions.cancel import cancel
from handler_functions.help import help

from handler_functions import states


# Hand over API_TOKEN to the bot
bot = telegram.Bot(token=API_KEY)


print(bot.get_me())
{"first_name": "The Coaching Bot", "username": "TheCoachingBot"}


# Runs the bot.
def main() -> None:
    # Creates the updater and passes the API_TOKEN to it.
    updater = Updater(API_KEY)

    # Gets the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # bot state machine(s)
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            states.BIO:         [MessageHandler(Filters.text & ~Filters.command, bio)],
            states.GENDER:      [MessageHandler(Filters.regex('^(Gentleman|Lady|Unicorn)$'), gender)],
            states.BIRTHDATE:   [MessageHandler(Filters.text & ~Filters.command, birthdate), CommandHandler('skip', skip_birthdate)],
            states.EMAIL:       [MessageHandler(Filters.text & ~Filters.command, email), CommandHandler('skip', skip_email)],
            states.TELEPHONE:   [MessageHandler(Filters.text & ~Filters.command, telephone), CommandHandler('skip', skip_telephone)],
            states.LOCATION:    [MessageHandler(Filters.location, location), CommandHandler('skip', skip_location)],
            states.PHOTO:       [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
            states.SUMMARY:     [MessageHandler(Filters.regex('^(COMPLETE SIGN UP)$'), summary)],
            # more states here...
        },
        fallbacks=  [CommandHandler('cancel', cancel)],
    )
    
    # dispatch conversation handlers
    dispatcher.add_handler(conv_handler) # /start, /cancel
    dispatcher.add_handler(Commandhandler('help', help)) # /help
    dispatcher.add_handler(Commandhandler('summary', summary)) # /help
    dispatcher.add_handler(Commandhandler('delete', delete)) # /help
    dispatcher.add_handler(Commandhandler('status', status)) # /help


    help_handler = ConversationHandler(
        entry_points=[CommandHandler('help', help)],
        states={
            HELP:               [MessageHandler(Filters.text & ~Filters.command, bio)],
        },
        fallbacks=  [CommandHandler('close', close)],

    # more Handlers here...

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
