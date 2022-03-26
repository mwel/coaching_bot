from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
    ConversationHandler, CallbackContext)

STATE01, STATE02 = range(4)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('Welcome Message')
    return STATE01

def state01(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text('Thank you! I hope we can talk again some day.')
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    update.message.reply_text('Bye! I hope we can talk again some day.', 
    reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main() -> None:
    updater = Updater("TOKEN")
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={STATE01: [MessageHandler(Filters.text & 
        ~Filters.command, state01)],},
        fallbacks=[CommandHandler('cancel', cancel)],)
    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()