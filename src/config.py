import codecs
import email
import json
import logging.config
import os

DB_NAME = "./db/dev.db"


with codecs.open(
    f"{os.path.dirname(__file__)}/logging.json", "r", encoding="utf-8-sig"
) as fd:
    logging.config.dictConfig(json.load(fd))

configuration = {
    "token": os.environ.get("BOT_TOKEN"),
    "logging_level": os.environ.get("LOGGING_LEVEL", "DEBUG").upper(),
}
