""" tests the calendar_manager.py functions """


# imports
from calendar_manager import authenticate, check_availability, make_appointment, cancel_appointment


" TESTS "

# can we authenticate agains google API?
# authenticate() #desired behaviour: "+++++ OAuth2 SUCCESSFUL +++++"


# can we check free slots?
check_availability()


# can we make an appointment
make_appointment('coaching Session') #userID hardcoded here


# is the appointment at a time, that is still available?


# can we delete an appointment?
# cancel_appointment()
