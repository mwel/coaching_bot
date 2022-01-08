# one constant per stage
BIO, GENDER, BIRTHDATE, EMAIL, TELEPHONE, LOCATION, PHOTO, SUMMARY  = range(8)

# translater of states from db response back to constants
def state_translator(state_number):
    switch={
      0:BIO,
      1:GENDER,
      2:BIRTHDATE,
      3:EMAIL,
      4:TELEPHONE,
      5:LOCATION,
      6:PHOTO,
      7:SUMMARY,
      8:'COMPLETED'
      }
    return switch.get(state_number,"NOT A STATE")


HELP = range(1)
