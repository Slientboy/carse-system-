# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

   API_ID_KEY = ''
    API_HASH_KEY = ''
    STRING_SESSION = ''
    HEROKU_API_KEY = ''
    HEROKU_APP_NAME = ''
    RAW_SIBYL = ''
    RAW_ENFORCERS = ''
    SIBYL = ''
    INSPECTORS = ''
    ENFORCERS = ''
    MONGO_DB_URL = ''
    Sibyl_logs = ''
    Sibyl_approved_logs = ''
    GBAN_MSG_LOGS = ''
    BOT_TOKEN = ''

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
