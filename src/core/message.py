from loguru import logger
from aiogram.types import Message

from config import Config


STOP_WORDS = Config().read_words()
logger.info(f"Parced words count: {len(STOP_WORDS)}")


class CustomMessage:
    """
    Custom message abstraction
    """

    message: Message

    def __init__(self, message: Message) -> None:
        """
        Initializing of CustomMessage

        :param message: Telegram Message
        """

        self.message = message

    async def add_to_filter(self) -> None:
        """
        Add word to filter
        """

        STOP_WORDS.append(self.message.text)

        with open("words.txt", "a", encoding="UTF-8") as file:
            file.write(f"\n{self.message.text}")

    async def is_filtered(self) -> bool:
        """
        Predict function to check if message is in filter
        """

        return self.message.text in STOP_WORDS

    async def filter(self) -> bool:
        """
        Filter message and delete it if it contains bad words
        """

        if "*" in self.message.text:
            await self.message.delete()
            return True

        message_words = self.message.text.split()

        for word in message_words:
            if word.lower() in STOP_WORDS:
                await self.message.delete()
                return True

        return False
