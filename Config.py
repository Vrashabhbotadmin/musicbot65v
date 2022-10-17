import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "21169898"))
    API_HASH = os.environ.get("API_HASH", "3bf3977ac2afcbefee5460e38c38135a")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5454352993:AAEbK8E8oVDGTeJj8VLqqLAmSc7rDvqOXFA")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBu0HiwRMiHEKcu8XSuaDmJhieNEjUEI-JhZYRiyq9csrukGyYGbKqDSYkrPAkyGrj0vo_slgjgLdYq4a1fdrC-NrWr8Sfl8ga5M4V-Cu3lbpw0d1t1nQSxxSEUzC5ExPenssrmjRqiaF0GNvkH855PRHBRYc2cuquMc4UNVVAIY5TXPeRDqKLlyQ3v7BaC4BSQqfH-IVXbYOSy_leYhiQ_c5PaAYLJ7qX3mIDX6_h8flPj2DW6gKluUp8flX5UTxCQyBDdReONB82Jk0IL6QsyAiqzacnhd3I2oA8TTMmnv2upOe8hEgSPUqFtrMVSM5JL1HhQtz4rerHpF9LMVzu2sg=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("Officimusic_bot")
    SUPPORT = os.environ.get("SUPPORT", "loggroupr") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "logchannelvi") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("5682847277")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
