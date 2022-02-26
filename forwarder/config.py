from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5263956969:AAGvGM6nZNEwOmjuGMbmP46a5L1unTjz-nw"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001352576623,-1001496083085]# List of chat id's to forward messages from.
    TO_CHATS = [-1001618760737]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
