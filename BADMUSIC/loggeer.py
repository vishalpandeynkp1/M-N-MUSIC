import logging
import pytz
import time
from pymongo import MongoClient
from config import LOG_FILE_NAME
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from Abg import patch
from motor.motor_asyncio import AsyncIOMotorClient as MongoCli
from pyrogram import Client
from logging.handlers import RotatingFileHandler
from pyrogram.enums import ParseMode
import config
import uvloop

uvloop.install()

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
SUKH2 = logging.getLogger(__name__)
boot = time.time()
mongodb = MongoCli(config.MONGO_DB_URI)
db = mongodb.Badmusic
mongo = MongoClient(config.MONGO_DB_URI)
OWNER = config.OWNER_ID


def SUKH2(name: str) -> logging.Logger:
    return logging.getLogger(name)
