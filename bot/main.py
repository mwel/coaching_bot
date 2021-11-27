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
import logging
import telegram
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import dateTime
import ConversationHandlers
from constants import API_KEY

# Hand over API_TOKEN to the bot
bot = telegram.Bot(token=API_KEY)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

print(bot.get_me())
{"first_name": "The Coaching Bot", "username": "TheCoachingBot"}

# took the definitions of "GENDER, PHOTO, LOCATION, BIO = range(4)", separated them and put them into their respective classes.

# took the function, that returns the gender and separated it into handler_functions.gender.py





# Stores the photo and asks for a location.
def photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    photo_file.download(user.first_name+'_photo.jpg')
    logger.info("Photo of %s: %s", user.first_name, user.first_name+'_photo.jpg')
    update.message.reply_text(
        'Gorgeous! Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, you can /skip this step.'
    )

    return LOCATION


# Skips the photo and asks for a location.
def skip_photo(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User << %s >> did not send a photo.", user.first_name)
    update.message.reply_text(
        'Ok, I\'ll take your word for it and bet you look great! ;)  \n\n'
        'Now, send me your location please, so I know where you are from. \n\n'
        'Just use Telegram\'s built in function to share your location with me once for the record. \n\n'
        'Or, if you prefer not to, just /skip this step.'
    )

    return LOCATION


# Stores the location and asks for some info about the user.
def location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    user_location = update.message.location
    logger.info(
        "Location of %s: %f / %f", user.first_name, user_location.latitude, user_location.longitude
    )
    update.message.reply_text(
        'Wow! I\'ve always wanted to go there - maybe I can visit sometime. \n\n'
        'At last, tell me a little bit about yourself, so I can get to know you better.'
    )

    return BIO


# Skips the location and asks for info about the user.
def skip_location(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s did not send a location.", user.first_name)
    update.message.reply_text(
        'Ok, you seem a bit paranoid, but then again - you can never be too careful!  \n\n'
        'Now, at last, tell me a little bit about yourself - otherwise this really doesn\'t make any sense. ;).'
    )

    return BIO


# Stores the info about the user and ends the conversation.
def bio(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("Bio of %s: %s", user.first_name, update.message.text)
    update.message.reply_text('Thank you so much for signing up! Coaching can change your life and you have just taken the first step in the right direction.')

    return ConversationHandler.END


# Cancels and ends the conversation.
def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s canceled the conversation.", user.first_name)
    update.message.reply_text(
        'APPLICATION TERMINATED by ' + user.first_name,
        'You ended the converstation and now have 2 options. Leave OR /start over.', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


# Runs the bot.
def main() -> None:
    # Passes the API_TOKEN to the Updater.
    updater = Updater(API_KEY)

    # Gets the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # removed conv handlers from here and separated them into ConversationHandlers.CH-Stage01.py

    dispatcher.add_handler(ConversationHandlers.conv_handler) #calling Handler from separate class
    # more Handlers here...

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
