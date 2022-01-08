from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update, context: CallbackContext):
    # Show the help text.

    header = '*coaching Bot HELP*\n\n'
    
    # add more help lines here
    help    = 'Call for help and it shall be displayed.\n'
    start   = 'Start The Coaching Bot.\n'
    summary = 'Ask the database for everything it has on you.'
    cancel  = 'End your conversation with the bot and delete all data your have submitted.\n'
    delete  = 'Delete all data you have ever submitted.\n'
    status  = 'Ask the bot how many steps you have left to complete your current stage.\n'
    
    # sum em up
    help_items = help + start + summary + cancel + delete + status

    # forge final string
    text = header + help_items 
    context.bot.send_message(chat_id=update.effective_user.id, text=text, parse_mode='Markdown')
    
