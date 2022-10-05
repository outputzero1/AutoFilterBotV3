import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'BQBDWW0law2yzHKgIQvjK2k93PdUHhWLB2S2YybTHKXC0ie1Y8AJ89yW4yO5PFkdB9W7eQ_pNSahm9M0AgcjNP9wrGzTdWhtGT5ESsVltmllOHuDDDnYNd2l5_8zTCYlbGSSQ05wercHl1oZLjgHbg6W1nncijbe1y_Sx55g6JL2aCHEpv9Dzm-TbKVuzkjWKHorlWsmRaphd4PN4yjFwcWR1R2-E9qvfVgdd8B-CxBOd8HDzJ_o0K0xFKIGQVBd__cQve6raZmWUakPHMelligQ-5_cbUItaSVuwS5x6NNIjYPZDtsXP_JyX_X4DFAHHA4VjK_bVYJ6NpFjdpnejA6rAAAAAUQqjEYA')
API_ID = int(environ['API_ID', '11004381'])
API_HASH = environ['API_HASH', '8e0588044fcf7672cfe1341185bfc94c']
BOT_TOKEN = environ['BOT_TOKEN', '5732081520:AAErJygtWmP8ETgwrydmBYQ49XtZOiOiYnQ']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

BROADCAST_CHANNEL = int(os.environ.get("BROADCAST_CHANNEL", ""))
ADMIN_ID = set(int(x) for x in os.environ.get("ADMIN_ID", "1260704822").split())
DB_URL = os.environ.get("DATABASE_1", "mongodb+srv://filterzflixbot: filterzflixbot@filterzflixbot.nj7hwtd.mongodb.net/?retryWrites=true&w=majority")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST", True))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('FORCES_SUB')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
TUTORIAL = "https://youtu.be/5hnYOKBzyi8"
# MongoDB information
DATABASE_URI = environ['DATABASE_2']
DATABASE_NAME = environ['BOT_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Auto Filter V3**

Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "http://www.omdbapi.com/?i=tt3896198&apikey=4f08a979")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
