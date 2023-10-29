import logging

from telethon import TelegramClient

from os import getenv
from AltBots.data import ALTRON


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


# VALUES REQUIRED FOR XBOTS
API_ID = 29499310
API_HASH = "d49ecebafbaa772a60404ec555b9cbb9"
CMD_HNDLR = getenv(".", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("6460262962:AAF2_EKwujowJYIc6IOocKmcIQfjaBcvjx4", default=None)
BOT_TOKEN2 = getenv("6739346442:AAHrv7JvJH3JkuyjVRK9l_8eHVNvA1wcRRU", default=None)
BOT_TOKEN3 = getenv("6795643222:AAEjx5lFtIUIU1TFilv1hhF-c9xcki1oDPk", default=None)
BOT_TOKEN4 = getenv("6816427422:AAF6ULTSLGRjXQ3ipuBnwRPQNHbYb6Jyth0", default=None)
BOT_TOKEN5 = getenv("6767746936:AAG09wIQNldKiM35hvZotqNGrBc_l9mfO8c", default=None)
BOT_TOKEN6 = getenv("6538530505:AAFoCGElhEPQuxojvmqU35gyv2sGHTZ6wl4", default=None)
BOT_TOKEN7 = getenv("6915607745:AAFAPQj3nSqGtfv4IbbJ70gvuj1Z5rTvKB0", default=None)
BOT_TOKEN8 = getenv("6746360736:AAG2tx-bVzq7ubAOHpJDVxsvUM-TIfO0VRo", default=None)
BOT_TOKEN9 = getenv("6559355457:AAEMQB26EGU0GMf0xtIrzmKGY1Mp4EODSeg", default=None)
BOT_TOKEN10 = getenv("6357647861:AAGbOmKJfn0zsKCnKN4bDCoRFyWZRFE4G08", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="5518687442").split()))
for x in ALTRON:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="5518687442"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
X2 = TelegramClient('X2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)
X3 = TelegramClient('X3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)
X4 = TelegramClient('X4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)
X5 = TelegramClient('X5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)
X6 = TelegramClient('X6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)
X7 = TelegramClient('X7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)
X8 = TelegramClient('X8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)
X9 = TelegramClient('X9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)
X10 = TelegramClient('X10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)
