import os

class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    MONGO_URI = os.environ.get("MONGO_URI")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "filterdb")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    ADMINS = [int(x) for x in os.environ.get("ADMINS", "").split()]
