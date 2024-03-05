import os
import json
import dotenv
import asyncio
import aiogram
from loguru import logger


dotenv.load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMINS = os.getenv("ADMINS").split()
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = aiogram.Bot(token=TOKEN)
dp = aiogram.Dispatcher()
stop_words = []
texts = {}

logger.add(
    sink="./log/app.log",
    level="DEBUG",
    format="[{time}][{level}]: {message} (line: {line})",
    rotation="1 MB",
    compression="zip",
)
logger.info("Initializing")


async def filter_message(
    *, user_chat_id: int, message_id: int, message_text: str
) -> bool:    
    if "*" in message_text:
        await bot.delete_message(user_chat_id, message_id)
        return True

    message_text_words = message_text.split()

    for word in message_text_words:
        if word in stop_words:
            await bot.delete_message(user_chat_id, message_id)
            return True

    return False


def read_texts(*, filepath: str = "texts.json") -> dict:
    with open(filepath, "r", encoding="utf-8") as file:
        return json.loads(file.read())


def read_words() -> list:
    with open("words.txt", "r", encoding="utf-8") as file:
        logger.info("Reading words file")

        return [word.strip("\n") for word in file.readlines() if word]


async def add_filter_word(*, word: str) -> None:
    stop_words.append(word)

    with open("words.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{word}")


@dp.edited_message()
@dp.message()
async def messages_handler(message: aiogram.types.Message) -> None:
    # Checking if message was received from the chat
    # Group chat id's are less than 0
    if message.chat.id < 0 and message.chat.type != "private":
        if message.chat.id != CHAT_ID or not message.text:
            return

        await filter_message(
            user_chat_id=message.chat.id,
            message_id=message.message_id,
            message_text=message.text.lower()
        )

        return

    # If message was once edited, we don't let it go next
    if message.edit_date:
        return

    # If message wasn't from group then this is private chat
    # Checking if message was received from admin
    # Because only admins can chat with bot.
    if str(message.chat.id) in ADMINS:
        if message.text[:14] == "/add_stop_word":
            if message.text[15:] in stop_words:
                await message.reply(
                    texts["admin"]["replies"]["error_word_already_exists"]
                )
            else:
                await add_filter_word(word=message.text[15:])
                await message.reply(
                    texts["admin"]["replies"]["success_word_added"]
                )

        elif message.text[:16] == "/check_stop_word":
            if message.text[17:] in stop_words:
                await message.reply(
                    texts["admin"]["replies"]["success_word_exists"]
                )
            else:
                await message.reply(
                    texts["admin"]["replies"]["error_word_doesnt_exists"]
                )

        await message.reply(texts["admin"]["replies"]["admin_menu"])
        return

    await message.reply(texts["admin"]["replies"]["error_admin_only"])


async def main() -> None:
    global stop_words, texts

    texts = read_texts()
    stop_words = read_words()
    logger.info(f"Words parced: {len(stop_words)=}")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
