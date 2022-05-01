import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6435225")
    API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    TOKEN = getenv("TOKEN", "5087493887:AAFTunel4Vr9-F1nb2vfueEoivJQJ2NZbzw")
    OWNER_ID = getenv("OWNER_ID", "1669178360")
    PYRO_SESSION = getenv("PYRO_SESSION", "AgCkZOg_VjR_XdXZyjbTpELUefGz0_ULlqw3kSuYVdGmtAGqYK7Q8JVO9A1auA2zXndpI4r048_Y-8sjVP8Vgx7dM1zdpTnMoLif8QujTsBaCacwYmWSsxfqrX0rx_DGSIRjdQpMHy5O-fzz7X7GuCABJEfNzXd2o4duaqWAZkrXJnZF9_b914FfbjMiSKNnIuFxwksRCFNvfn9YuQAMHExiQ1_yfCYcOd22QC6BmcZ33Z5s6UBItTNa0A18-6VwadjQ82irHLp6K65E0B-yUE7yg_ePozO6zmrwxDQsCxVeZwRc5A-mNHhZviUDpDZP-v3Gz-Vra5ww4rjN2fDkxlVMAAAAATKAVEIA")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
    DB_URI = getenv("DATABASE_URL", "postgresql://ffmrqpix:wMMlyGU05RgTnTq4Ngs7KkuMh8W1X4gs@chunee.db.elephantsql.com/ffmrqpix")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001509525202")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001509525202")
    SYS_ADMIN = getenv("SYS_ADMIN", "1669178360")
    DEV_USERS = getenv("DEV_USERS", "1669178360")
    LOAD = getenv("LOAD")
    NO_LOAD = None
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CASH_API_KEY = getenv("CASH_API_KEY", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("TIME_API_KEY", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("BOT_API_URL", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("BOT_API_FILE_URL", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("DEV_USERS", "1669178360").split()))
