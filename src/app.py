import os
import dotenv
import asyncio
import aiogram
from loguru import logger


dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher()
stop_words = []

logger.add(
    sink="./log/app.log",
    level="DEBUG",
    format="[{time}][{level}]: {message} (line: {line})",
    rotation="1 MB",
    compression="zip",
)
logger.info("Initializing")


with open("words.txt", "r", encoding="utf-8") as file:
    logger.info("Reading words file")

    stop_words = [word.strip("\n") for word in file.readlines() if word]

    logger.info(f"Words parced: {len(stop_words)=}")


async def filter_message(
    *, user_chat_id: int, message_id: int, message_text: str
) -> bool:
    message_text_words = message_text.split()

    for word in message_text_words:
        if word in stop_words:
            await bot.delete_message(user_chat_id, message_id)
            return True

    return False


@dp.message()
async def messages_handler(message: aiogram.types.Message) -> None:
    if message.chat.id == CHAT_ID:
        await filter_message(
            user_chat_id=message.chat.id,
            message_id=message.message_id,
            message_text=message.text,
        )


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
