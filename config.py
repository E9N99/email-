import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 8897410))

    API_HASH = os.environ.get("API_HASH", "43cb89a7b70782868b77ace21c1341a9")
