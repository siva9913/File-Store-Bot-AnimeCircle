#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6719671139:AAGxNgP9P9E0JofbPTZIKlVcrb-6n1bqGwM")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "5540967"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "eedf0196b0533f361b51b5b7082358e9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002002878785"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "669038293"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://daniel811802:0wQNzmwMkUiqOZa1@cluster0.8jaksiw.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002108086258"))
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001568945878"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hᴇʟʟᴏ, {first} 👋\n\n<b>I ᴀᴍ Oɴʟʏ Sᴛᴏʀᴇ ғɪʟᴇs ғᴏʀ <a href='https://t.me/chatbox480'>Aɴɪᴍᴇ Cɪʀᴄʟᴇ ™</a></b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "669038293").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channels to use me\n\nKindly Please join Channels</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>I ᴀᴍ Oɴʟʏ Sᴛᴏʀᴇ ғɪʟᴇs ғᴏʀ <a href='https://t.me/chatbox480'>Aɴɪᴍᴇ Cɪʀᴄʟᴇ ™</a>\n\nFor More Info Click: /start</b>\n"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
