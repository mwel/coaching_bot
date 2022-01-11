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
# def validate_email(input):

#     print(f'----- Input submitted for validation: {input} -----')
 
#     format = re.compile(r'(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])')

#     print(f'format: {format}')

#     isValid = True
#     if re.fullmatch(format, input):
#         print(f'----- Format accepted: {input} -----')
#     else:
#         print(f'----- NOT a telephone number: {input} -----')
#         isValid = False

#     return isValid


# validates telephone number for format +00 0000000000
def validate_telephone(input): 

    print(f'----- Input submitted for validation: {input} -----')
 
    format = re.compile(r'^\+4[139]\d{9,12}$') # regex for telephone numbers for GERMANY, AUSTRIA, SWITZERLAND with 9 to 12 digit phone numbers - adapt to country (also in main conv handler)

    print(f'format: {format}')

    isValid = True
    if re.fullmatch(format, input):
        print(f'----- Format accepted: {input} -----')
    else:
        print(f'----- NOT a telephone number: {input} -----')
        isValid = False

    return isValid

