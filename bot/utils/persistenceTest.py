from collections import defaultdict
from telegram.ext import BasePersistence
from telegram.ext.utils.types import ConversationDict

class PersistenceTest (BasePersistence):
    def __init__(self, store_user_data, store_chat_data, store_bot_data, store_callback_data):
        super().__init__(store_user_data=store_user_data, store_chat_data=store_chat_data, store_bot_data=store_bot_data, store_callback_data=store_callback_data)

    def get_bot_data(self):
        print ("Called: get_bot_data()")
        return defaultdict(dict)

    def update_bot_data(self, data):
        print (f"Called: update_bot_data(data) {str(data)})")

    def refresh_bot_data(self, bot_data): #called before command is handled (user interaction)
        print (f"Called: refresh_bot_data(bot_data: {str(bot_data)})")

    def get_chat_data(self): #method that writes data from db back into the bot upon restart
        # ask db for data. if there is data, return
        print ("Called: get_chat_data()")
        return defaultdict(dict)

    def update_chat_data(self, chat_id, data): #called after command is handled (user interaction)
        print (f"Called: update_chat_data(chat_id: {chat_id}, data: {str(data)})")

    def refresh_chat_data(self, chat_id, data): #called before command is handled (user interaction)
        print (f"Called: refresh_chat_data(chat_id: {chat_id}, data: {str(data)})")

    def get_user_data(self): #method that writes data from db back into the bot upon restart
        # ask db for data. if there is data, return
        print ("Called: get_user_data()")
        # call from here another class with another method, that takes care of the db query and writed the data back into the dictionary, that should be returned from this method.
        user_data = defaultdict(dict) 
        # now get data from db and hand it write it into the empty dict, you just created... like so:
        # add User data from DB here in the form user_data[user_id]=user_data_as_dict
        user_data[222987147] = {'status': 'Phrittus'} # This is how you add user data
        return user_data

    def update_user_data(self, user_id, data): #called after command is handled (user interaction)
        print (f"Called: update_user_data(user_id: {user_id}, data: {str(data)})")

    def refresh_user_data(self, user_id, data): #called before command is handled (user interaction)
        print (f"Called: refresh_user_data(user_id: {user_id}, data: {str(data)})")

    def get_callback_data(self):
        print ("Called: get_callback_data()")
        return defaultdict(dict)

    def update_callback_data(self, data): #called after command is handled (user interaction) // empty / not used
        print (f"Called: update_callback_data(data: {str(data)})")

    def get_conversations(self, name):
        print (f"Called: get_conversations(name: {name})")
        return defaultdict(dict)

    def update_conversation(self, name, key, new_state):
        print (f"Called: update_conversation(name: {name}, key: {str(key)}, new_state: {str(new_state)})")

    def flush(self): #called when bot is shut down to allow db / user_dict to finish operation
        print ("Called: flush()")
