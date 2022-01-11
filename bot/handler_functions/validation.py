""" input validation functions check user input for various criteria approve or deny an entry"""

# imports
import datetime
import re


# validates birthdate for format DD-MM-YYYY
def validate_birthdate(input): 

    print(f'----- Input submitted for validation: {input} -----')
    format = '%d.%m.%Y'

    isValid = True
    try:
        date_time = datetime.datetime.strptime(input, format)
        print(f'----- Format accepted: {date_time} -----')
    
    except ValueError:
        print(f'----- NOT a birthdate: {input} -----')
        isValid = False

    return isValid


# validates email address for format accountname@domain.com
def validate_email(input):

    print(f'----- Input submitted for validation: {input} -----')
 
    format = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    isValid = True
    if re.fullmatch(format, input):
        print(f'----- Format accepted: {input} -----')
    else:
        print(f'----- NOT an email address: {input} -----')
        isValid = False

    return isValid


# validates telephone number for format +00 0000000000
def validate_telephone(input): 

    print(f'----- Input submitted for validation: {input} -----')
 
    format = re.compile(r'^\+4[139]\d{9,12}$') # regex for telephone numbers for GERMANY, AUSTRIA, SWITZERLAND with 9 to 12 digit phone numbers - adapt to country (also in main conv handler)

    isValid = True
    if re.fullmatch(format, input):
        print(f'----- Format accepted: {input} -----')
    else:
        print(f'----- NOT a telephone number: {input} -----')
        isValid = False

    return isValid

