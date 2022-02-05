""" tests the calendar_manager.py functions """


# imports
import bot.handler_functions.calendar.calendar_manager as calendar_manager


" TESTS "

# can we authenticate agains google API?
# calendar_manager.authenticate() #desired behaviour: "+++++ OAuth2 SUCCESSFUL +++++"


# can we check free slots?
calendar_manager.check_availability()


# can we make an appointment
calendar_manager.make_appointment(28648774, 'coaching Session') #userID hardcoded here


# is the appointment at a time, that is still available?


# can we delete an appointment?
# calendar_manager.cancel_appointment()
