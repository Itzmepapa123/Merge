import os


class Config(object):
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", None)
    IS_PREMIUM = False
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "root")
    MODES = ["video-video", "video-audio", "video-subtitle", "extract-streams"]
    API_HASH = "fa4c3f582286d969ab1d08449e9533e8"
    BOT_TOKEN = "7277558508:AAGq41OAe9SchpFgj115FUHZMHY7oV_1qoE"
    TELEGRAM_API = "21310924"
    OWNER = "7030439873"
    OWNER_USERNAME = "Mr_Bankaiiii"
    PASSWORD = "Bankai Op"
    DATABASE_URL = "mongodb+srv://itzmeproman:itzmeproman@cluster0.4v4f5ao.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    LOGCHANNEL = "-1002174195692"    # Premium account session string to upload upto 4GB (requires "LOGCHANNEL")
    
    UPSTREAM_REPO = "https://github.com/Itzmepapa123/Merge"
    UPSTREAM_BRANCH = "master"
