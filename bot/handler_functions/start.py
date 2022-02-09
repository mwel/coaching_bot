""" start handler function. called, when the bot is started (user enters /start) """

# imports
from datetime import datetime
from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler
from logEnabler import logger;


from handler_functions import states
from handler_functions.database_connector.insert_value_db import insert_update
from handler_functions.database_connector import select_db
from handler_functions.database_connector.create_db import create_db


# Starts the conversation and continues on to the next state
def start(update: Update, context: CallbackContext) -> int:

    # CREATE DB, IF NOT EXISTS
    create_db()

    user_id = update.message.from_user.id

    user_exists = select_db.user_search(user_id)  # maybe also check, whether there is a db value saved in 'state'
    if user_exists:
        # get user's state from db
        state = int(select_db.get_value(user_id, 'state'))

        update.message.reply_text(
            f'Welcome back {update.message.from_user.first_name},\n'
            'Let\'s continue where we left off...',
            # '(In case you would like to start over, just /cancel and /start again.)',
            reply_markup=ReplyKeyboardRemove(),
            )

        if state == states.SUMMARY:  # sign up was apparently already completed for this user
            reply_keyboard = [
                ['/status'], 
                ['/summary'],
                ['/delete']]
            update.message.reply_text(
           'Ah! I see, you have already completed the sign up.\nYou now have multiple options below:\n'
           'If you have not made an appointment yet and would like to do so, reenter /summary.\n\n'
           'If you want to /delete your record entirely, press /delete.',
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='SIGN UP COMPLETE'
                )
            )

        elif state == states.APPOINTMENT and select_db.get_value(user_id, 'appointment') == 'None':

            reply_keyboard = [
                ['/status'], 
                ['/delete']]
            update.message.reply_text(
            'If you have not made an appointment yet and would like to do so, enter /summary.\n\n',
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='SIGN UP COMPLETE'
            )
        )
            return ConversationHandler.END

        elif state == states.APPOINTMENT:

            appointment_made = select_db.get_value(user_id, 'appointment')
            reply_keyboard = [
                ['/cancel_appointment'], 
                ['/status'], 
                ['/delete']]
            update.message.reply_text(
            f'Cool. You already have an appointment on {appointment_made} \n\n'
            'In case you would like to cancel, just enter /cancel_appointment.\n\n'
            'Otherwise, we are looking forward to our call.',
            reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='SIGN UP COMPLETE'
            )
        )
            return ConversationHandler.END
        
        # call next function for user
        update.message.reply_text(states.MESSAGES[state], reply_markup=states.KEYBOARD_MARKUPS[state])
        return state


    logger.info(f'+++++ NEW USER: {update.message.from_user.first_name} {update.message.from_user.last_name} +++++')

    # write user info to db
    insert_update(user_id, 'first_name', update.message.from_user.first_name) # saving of user_id not necessary, because it will be saved here anyway.
    insert_update(user_id, 'last_name', update.message.from_user.last_name)
    insert_update(user_id, 'appointment', 'None')
    insert_update(user_id, 'event_id', '0')
    # insert_update(user_id, 'state', 0) # set state to 0 in case user does not even complete step 1, leaves and returns later.
    # insert_update(user_id, 'phone_number', update.message.from_user.phone_number) # TODO: figure out how to get user's phone number
    # >> safe more initial variables about the user here.

    update.message.reply_text(
        f'Hi {update.message.from_user.first_name},\n'
        'I am a coaching bot by wavehoover. You have taken the first step on your journey to success by contacting me. I will guide you through the application process for your first coaching session. '
        'It\'s super easy. Just follow the questions, answer or skip them - that\'s it.\n\n'
        '[You can send /cancel at any time, if you are no longer interested in a conversation.]\n\n'
        f'Now, {update.message.from_user.first_name} - {states.MESSAGES[states.BIO]}',
        reply_markup=ReplyKeyboardRemove(),
        )

    # save state to DB
    insert_update(user_id, 'time_stamp', datetime.now())
    insert_update(user_id, 'state', states.BIO)
    return states.BIO
