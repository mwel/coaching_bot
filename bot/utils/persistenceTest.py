from telegram.ext import BasePersistence

class PersistenceTest (BasePersistence):
    def __init__ (store_user_data, store_chat_data, store_bot_data, store_callback_data):
        super().__init__(store_user_data=store_user_data, store_chat_data=store_chat_data, store_bot_data=store_bot_data, store_callback_data=store_callback_data)


    def get_bot_data():
        print ("Called: get_bot_data()")

    def update_bot_data(data):
        print (f"Called: update_bot_data(data) {str(data)})")

    def refresh_bot_data(bot_data):
        print (f"Called: refresh_bot_data(bot_data: {str(bot_data)})")

    def get_chat_data():
        print ("Called: get_chat_data()")

    def update_chat_data(chat_id, data):
        print (f"Called: update_chat_data(chat_id: {chat_id}, data: {str(data)})")

    def refresh_chat_data(chat_id, data):
        print (f"Called: refresh_chat_data(chat_id: {chat_id}, data: {str(data)})")

    def get_user_data():
        print ("Called: get_user_data()")

    def update_user_data(user_id, data):
        print (f"Called: update_user_data(user_id: {user_id}, data: {str(data)})")

    def refresh_user_data(user_id, data):
        print (f"Called: refresh_user_data(user_id: {user_id}, data: {str(data)})")

    def get_callback_data():
        print ("Called: get_callback_data()")

    def update_callback_data(data):
        print (f"Called: update_callback_data(data: {str(data)})")

    def get_conversations(name):
        print (f"Called: get_conversations(name: {name})")

    def update_conversation(name, key, new_state):
        print (f"Called: update_conversation(name: {name}, key: {str(key)}, new_state: {str(new_state)})")

    def flush():
        print ("Called: flush()")
