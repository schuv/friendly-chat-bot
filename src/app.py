import asyncio

from loguru import logger
from aiogram.types import Message
from aiogram.fsm.state import default_state
from aiogram.exceptions import TelegramBadRequest
from aiogram import (
    Bot,
    Dispatcher
)

from config import Config
from admin.router import router
from admin.keyboard import MENU
from core.message import CustomMessage


dp = Dispatcher()


@dp.startup()
async def on_startup(bot: Bot):
    """
    Function that triggers on bot startup

    :param bot: Current bot instance
    """

    logger.info("Bot started")

    for admin in Config.admins:
        try:
            await bot.send_message(admin, "🟢 Бот начал работу")
        except TelegramBadRequest as e:
            logger.exception(e)


@dp.edited_message(default_state)
@dp.message(default_state)
async def message_handler(message: Message) -> None:
    """
    Handler to all the message from default state

    :param message: Telegram Message
    """

    if message.chat.type != "private":
        if message.chat.id != Config.chat_id or not message.text:
            return

        await CustomMessage(message).filter()
        return

    if message.edit_date:
        return

    if str(message.from_user.id) in Config.admins:
        await message.answer(
            Config.texts["ADMIN"]["GENERAL"],
            reply_markup=MENU
        )

        return

    await message.answer(Config.texts["ADMIN"]["ACCESS_DENIED"])


async def main() -> None:
    """
    Entry point
    """

    logger.info("Starting bot")

    dp.include_router(router)

    await dp.start_polling(Bot(token=Config.token))


if __name__ == "__main__":
    asyncio.run(main())
