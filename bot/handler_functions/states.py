"""Define states, state transition messages and keyboards."""

from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup

# STATE DEFINITIONS
MAX_STATES = 10
# one constant per stage
BIO, GENDER, BIRTHDATE, EMAIL, TELEPHONE, LOCATION, PHOTO, SUMMARY, COMPLETED, APPOINTMENT = range(MAX_STATES)


# transition messages to display at first encounter and at pick-up when continuing
MESSAGES = {
    
    BIO: 'Tell me a little bit about yourself - why are you here, what are your goals and what do you expect yourself from this journey?'
    ,
    
    GENDER: 'Would you like to be referred to as lady, gentleman or unicorn?'
    ,
    
    BIRTHDATE: 'Tell me - when is your birthday?'
    ,
    
    EMAIL: 'Please send me your email address, so I can send you your summary of submitted data upon completion.'
    ,
    
    TELEPHONE: 'One of the prep steps for your first face to face session is a quick phone call. '
        'In order for your coach to be able to give you a call, please send me a phone number, we can reach you under:'
    ,
    
    LOCATION: 'Alright - let\'s continue... '
        'I\'m from Switzerland. It\'s really nice here! Where are you from?\n\n'
        '- > Tip: Use Telegram\'s built in function to share your location with me.\n\n'
        'Or, if you prefer not to, just /skip this step.'
    ,
    
    PHOTO: 'Here is a picture of me - can you send one of you?'
    ,

    SUMMARY: 'You are now at the end of the sign up. Would you like to submit or /cancel and delete all your data?'
    ,

    COMPLETED: 'What\'s next? \n'
        'You will receive an email with this summary as confirmation.'
    ,

    APPOINTMENT: 'If you want to make an appointment for your first session, you can now do so by selecting one of the options below:\n\n'
        'If you would not like to make an appointment, just leave the chat.\n\n'
        'If you would like to reset your request and delete all your data, just enter /delete.'
    ,

}

# custom keyboards for next state
KEYBOARD_MARKUPS = {
    
    BIO: None,
    
    GENDER: ReplyKeyboardMarkup(
            [['Gentleman', 'Lady', 'Unicorn']], 
            one_time_keyboard=True, 
            input_field_placeholder='Lady? Gentleman? Unicorn? ... here you can be whatever you want.'
    ),
    
    BIRTHDATE: ReplyKeyboardMarkup(
            [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['/', '0', '.']
            ],
            input_field_placeholder='DD.MM.YYYY'
    ),
        
    
    EMAIL: None,
    
    TELEPHONE: ReplyKeyboardMarkup(
            [
            ['7', '8', '9'],
            ['4', '5', '6'],
            ['1', '2', '3'],
            ['+', '0', '#']
            ],
            input_field_placeholder='+00 000000000'
    ),
    
    LOCATION: None,
    
    PHOTO: None,

    SUMMARY: ReplyKeyboardMarkup(
            [['COMPLETE SIGN UP'], ['/delete']],
            input_field_placeholder='COMPLETE SIGN UP'
    ),

    APPOINTMENT: ReplyKeyboardMarkup(
            [['date1', 'date2', 'date3']], 
            one_time_keyboard=True, 
            input_field_placeholder='Choose your appointment...'
    ),

}


# default reply_text for handler functions
# update.message.reply_text(
#     'bla bla \n' + \
#     states.MESSAGES[states.GENDER],
#     reply_markup=states.KEYBOARD_MARKUPS[states.GENDER],
#     )


# reply_markup=ReplyKeyboardRemove(),
