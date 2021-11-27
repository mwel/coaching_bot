#!/usr/bin/env python

# This class will return a specific date dependant on the current date and on the function called.
# These dates are needed in the main for deadline purposes.

import datetime


# return today
def thisDay() -> datetime:
    today = datetime.date.today()
    print("Current date and time:")
    print(today)
    return today


# return date in 1 week
def oneWeek() -> datetime:
    oneW = datetime.timedelta.days
    print("You have until:")
    print(oneW)
    return oneW


# return date in 2 weeks
def twoWeeks() -> datetime:
    twoW = datetime.timedelta.days
    print("You have until: ")
    print(twoW)
    return twoW
