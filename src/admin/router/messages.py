from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import Config
from admin.states import AdminPanel
from admin.methods import AdminMethods
from core.message import CustomMessage


router = Router(name="Administrator messages")


@router.message(AdminPanel.new_word)
@AdminMethods.check_admin()
async def message_new_word_handler(
    message: Message,
    state: FSMContext
) -> None:
    """
    Handler to all the messages in ```AdminPanel new-word``` state.

    Adding new message to filter

    :param message: Telegram Message
    :param state: User State
    """

    custom_message = CustomMessage(message)
    filtered = await custom_message.is_filtered()

    if filtered:
        await message.reply(Config.texts["ADMIN"]["ADD_WORD"]["EXISTS"])
    else:
        await message.reply(Config.texts["ADMIN"]["ADD_WORD"]["ADDED"])
        await custom_message.add_to_filter()

    await state.clear()


@router.message(AdminPanel.check_word)
@AdminMethods.check_admin()
async def message_check_word_handler(
    message: Message,
    state: FSMContext
) -> None:
    """
    Handler to all the messages in ```AdminPanel check-word``` state.

    Checking if message is already in filtered

    :param message: Telegram Message
    :param state: User State
    """

    filtered = await CustomMessage(message).is_filtered()

    if filtered:
        await message.reply(Config.texts["ADMIN"]["CHECK_WORD"]["EXISTS"])
        return

    await message.reply(Config.texts["ADMIN"]["CHECK_WORD"]["NO_EXIST"])
    await state.clear()
