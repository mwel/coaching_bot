# one constant per stage
BIO, GENDER, BIRTHDATE, EMAIL, TELEPHONE, LOCATION, PHOTO, SUMMARY  = range(8)


def state_translator(state_number):
    switch={
      0:BIO,
      1:GENDER,
      2:BIRTHDATE,
      3:EMAIL,
      4:TELEPHONE,
      5:LOCATION,
      6:PHOTO,
      7:SUMMARY
      }
    return switch.get(state_number,"NOT A STATE")
