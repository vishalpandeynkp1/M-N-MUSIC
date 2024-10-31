
import logging
from logging.handlers import RotatingFileHandler
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pymongo import MongoClient
from pyrogram import Client
from pyrogram.enums import ParseMode

import config
import time


# welcome..
logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)
boot = time.time()
mongodb = MongoCli(config.MONGO_DB_URI)
db = mongodb.Badmusic
mongo = MongoClient(config.MONGO_DB_URI)
OWNER = config.OWNER_ID

