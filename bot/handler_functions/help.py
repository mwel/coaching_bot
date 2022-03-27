""" help function. called, when user enters /help """

# imports
from telegram import Update
from telegram.ext import ConversationHandler, CallbackContext

import collections
from handler_functions.cancel import cancel
from handler_functions.states import SUMMARY


def help(update: Update, context: CallbackContext):

    # header text    
    header = '*coaching Bot HELP*\n\n'

    # open a new ordered dictionay    
    help_dict = collections.OrderedDict({})

    # commands
    help_dict['help'] = 'Call for help and it shall be displayed.\n'
    help_dict['start'] = 'Start your conversation with The Coaching Bot or pick up, where you left off.\n'
    help_dict['cancel'] = 'End your conversation with the bot and delete all data you have submitted.\n (Only works, if you started the bot.)'
    help_dict['status'] = 'Ask the bot how many steps you have left to complete the sign up.\n'
    help_dict['summary'] = 'Ask the database for everything it has on you.\n'
    help_dict['delete'] = 'Delete all your data.\n (If you do, you have to /start over.) \n'
    # help_dict[''] = '' # add more help here


    # build final string
    help_items = ['/' + key + ' - ' + value for key, value in help_dict.items()]
    help_text = '\n'.join(help_items)
    text = header + help_text
    
    # send help text
    context.bot.send_message(chat_id=update.effective_user.id, text=text, parse_mode='Markdown')
    
    return ConversationHandler.END
