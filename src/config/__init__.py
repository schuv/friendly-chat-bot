import os
import json

from loguru import logger
from dotenv import (
    load_dotenv,
    find_dotenv
)


logger.add(
    sink="./log/app.log",
    level="INFO",
    format="[{time}][{level}]: {message} (line: {line})",
    rotation="1 MB",
    compression="zip",
)
logger.info("Initializing")
load_dotenv(
    dotenv_path=find_dotenv(".env"),
    override=True
)


class Config:
    """
    Config settings abstraction
    """

    token: str = os.getenv("BOT_TOKEN")
    texts: dict = json.load(open("/config/texts.json", "r", encoding="UTF-8"))
    admins: list = os.getenv("ADMINS").split()
    chat_id: int = int(os.getenv("CHAT_ID"))
    words_file: str = "/config/words.txt"

    def read_words(self) -> list:
        """
        Read all the bad words from special file
        """

        with open(self.words_file, "r", encoding="utf-8") as file:
            logger.info("Reading words file")

            return [word.strip("\n") for word in file.readlines() if word]
