""" help handler function. called, when user enters /help """

# imports
from telegram import Update
from telegram.ext import CallbackContext


# Show the help text.
def help(update: Update, context: CallbackContext):

    # header text    
    header = '*coaching Bot HELP*\n\n'
    
    # commands
    help    = 'Call for help and it shall be displayed.\n'
    start   = 'Start The Coaching Bot.\n'
    summary = 'Ask the database for everything it has on you.'
    cancel  = 'End your conversation with the bot and delete all data your have submitted.\n'
    delete  = 'Delete all data you have ever submitted.\n'
    status  = 'Ask the bot how many steps you have left to complete your current stage.\n'
    
    #  build a list in the order you like.
    text = [header, help, start, summary, cancel, delete, status] # TODO: needs fixing and formatting

    # forge final string
    context.bot.send_message(chat_id=update.effective_user.id, text=text) # cut out as last argument: "parse_mode='Markdown'"
    