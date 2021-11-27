# imports
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
from bot.handler_functions.start import GENDER, start
from bot.handler_functions.bio import bio
from bot.handler_functions.gender import PHOTO, gender
from bot.handler_functions.photo import LOCATION, photo
from bot.handler_functions.skip_photo import LOCATION, skip_photo
from bot.handler_functions.location import BIO, location
from bot.handler_functions.skip_location import BIO, skip_location
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