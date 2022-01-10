"""Define states, state transition messages and keyboards."""

from telegram import ReplyKeyboardMarkup

# STATE DEFINITIONS
MAX_STATES = 9
# one constant per stage
BIO, GENDER, BIRTHDATE, EMAIL, TELEPHONE, LOCATION, PHOTO, SUMMARY, COMPLETED = range(MAX_STATES)


# transition messages to display at first encounter and at pick-up when continuing
MESSAGES = {
    BIO: 'Tell me a little bit about yourself - we want to get to know you a little better in order to provide you with the best coaching experience possible.',
    GENDER: 'Would you like to be referred to as lady, gentleman or unicorn?',
    BIRTHDATE: 'tell me - when is your birthday?',
    EMAIL: 'Tolle EMAIL message!',
    TELEPHONE: 'Tolle TELEPHONE message!',
    LOCATION: 'Tolle LOCATION message!',
    PHOTO: 'Tolle PHOTO message!',
}


# custom keyboards for next state
KEYBOARDS = {
    BIO: None,
    GENDER: ReplyKeyboardMarkup(
            [['Gentleman', 'Lady', 'Unicorn']], one_time_keyboard=True, input_field_placeholder='Lady? Gentleman? Unicorn? ... here you can be whatever you want.'
        ),
    BIRTHDATE: None,
    EMAIL: None,
    TELEPHONE: None,
    LOCATION: None,
    PHOTO: None,
}
