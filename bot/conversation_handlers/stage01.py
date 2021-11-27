# imports
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from bot.handler_functions.gender import start

from bot.main import GENDER, PHOTO, LOCATION, BIO;
from bot.handler_functions.bio import bio
from bot.handler_functions.gender import gender
from bot.handler_functions.photo import photo
from bot.handler_functions.skip_photo import skip_photo
from bot.handler_functions.location import location
from bot.handler_functions.skip_location import skip_location
from bot.handler_functions.cancel import cancel


# Adds conversation handler with the states GENDER, PHOTO, LOCATION and BIO for stage 1 of the sign up
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        GENDER: [MessageHandler(Filters.regex('^(Gentleman|Lady|I am a unicorn.)$'), gender)],
        PHOTO: [MessageHandler(Filters.photo, photo), CommandHandler('skip', skip_photo)],
        LOCATION: [
            MessageHandler(Filters.location, location),
            CommandHandler('skip', skip_location),
        ],
        BIO: [MessageHandler(Filters.text & ~Filters.command, bio)],
    },
    fallbacks=[CommandHandler('cancel', cancel)],
)