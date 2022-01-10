""" help handler function. called, when user enters /help """

# imports
from telegram import Update
from telegram.ext import CallbackContext


from handler_functions.cancel import cancel
from handler_functions.states import SUMMARY


# Show the help text.
def help(update: Update, context: CallbackContext):

    # header text    
    header = '*coaching Bot HELP*\n\n'
    
    # commands
    COMMANDS = {
    HELP: 'Call for help and it shall be displayed.\n',
    START: 'Start The Coaching Bot.\n',
    SUMMARY: 'Ask the database for everything it has on you.',
    CANCEL: 'End your conversation with the bot and delete all data your have submitted.\n',
    DELETE: 'Delete all data you have ever submitted.\n',
    STATUS: 'Ask the bot how many steps you have left to complete your current stage.\n',
    }

    #  build a list in the order you like.
    text = [header, COMMANDS] # TODO: needs fixing and formatting

    # forge final string
    context.bot.send_message(chat_id=update.effective_user.id, text=text) # cut out as last argument: "parse_mode='Markdown'"
    