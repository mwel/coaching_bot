# data base tests
# from database_connector import create_db, select_db, insert_update_db, delete_record_db, insert_value_db
from handler_functions.database_connector import select_db


# insert_update_db.insert_update(
#     user_id=123456789,
#     first_name='Michael',
#     last_name='Müller',
#     gender='male',
#     photo='01010101010101010101',
#     birthdate='19900101',
#     email='test@gmx.de',
#     phone='+41123456789',
#     longitude='65432345678.00',
#     latitude='65432345678.00',
#     bio = 'Ich wurde als Phritte gebohren. Doch also selche krepieren soll ich nicht!',
#     state = '-1'
#     )

# insert_value_db.insert_update(123456789, 'first_name', 'Tüb')

# select_db.get_all_data(28648774)

# select_db.get_value(28648774, 'state')

select_db.user_search(28648774)