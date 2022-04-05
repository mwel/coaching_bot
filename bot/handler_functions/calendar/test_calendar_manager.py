""" tests the calendar_manager.py functions """


# imports
from calendar_manager import authenticate, check_availability, make_appointment, find_slots, main


" TESTS "

# test main function
# main()

# can we authenticate agains google API?
authenticate() #desired behaviour: "+++++ OAuth2 SUCCESSFUL +++++"


# can we check free slots?
# find_slots()


# can we make an appointment
# make_appointment('coaching Session') #userID hardcoded here


# is the appointment at a time, that is still available?


# can we delete an appointment?
# cancel_appointment()


{"timeMin": "2022-02-07T08:00:00Z", "timeMax": "2022-02-07T09:00:00Z", "items": [{"id": "84qo0c5ctm3e6p2cioh2c11iqc"}]}