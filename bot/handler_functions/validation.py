""" input validation functions check user input for various criteria approve or deny an entry"""

# imports
import datetime
import re


# validates birthdate for format DD-MM-YYYY
def validate_birthdate(input): 

    print(f'----- Input submitted for validation: {input} -----')
    format = '%d.%m.%Y'

    isValidDate = True
    try:
        date_time = datetime.datetime.strptime(input, format)
        print(f'----- Format accepted: {date_time} -----')
    
    except ValueError:
        print(f'----- NOT a birthdate: {input} -----')
        isValidDate = False

    return isValidDate


# def validate_email():


# validates telephone number for format +00 0000000000
def validate_telephone(input): 

    print(f'----- Input submitted for validation: {input} -----')
 
    format = re.compile(r'^\+4[139]\d{9,12}$') # regex for telephone numbers for GERMANY, AUSTRIA, SWITZERLAND with 9 to 12 digit phone numbers - adapt to country (also in main conv handler)

    print(f'format: {format}')

    isValidDate = True
    if re.fullmatch(format, input):
        print(f'----- Format accepted: {input} -----')
    else:
        print(f'----- NOT a telephone number: {input} -----')
        isValidDate = False

    return isValidDate

