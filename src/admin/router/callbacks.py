from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import (
    F,
    Bot,
    Router
)

from config import Config
from admin.states import AdminPanel
from admin.methods import AdminMethods


router = Router(name="Administrator callbacks")


@router.callback_query(F.data == "CHECK_WORD")
@AdminMethods.check_admin()
async def callback_check_word_handler(
    callback: CallbackQuery,
    bot: Bot,
    state: FSMContext
) -> None:
    """
    Handler for CHECK_WORD callback query

    :param callback: Telegram CallbackQuery
    :param bot: Current Bot instance
    :param state: User State
    """

    await state.set_state(AdminPanel.check_word)
    await bot.send_message(
        callback.from_user.id,
        Config.texts["ADMIN"]["CHECK_WORD"]["ENTER"]
    )


@router.callback_query(F.data == "NEW_WORD")
@AdminMethods.check_admin()
async def callback_new_word_handler(
    callback: CallbackQuery,
    bot: Bot,
    state: FSMContext
) -> None:
    """
    Handler for NEW_WORD callback query

    :param callback: Telegram CallbackQuery
    :param bot: Current Bot instance
    :param state: User State
    """

    await state.set_state(AdminPanel.new_word)
    await bot.send_message(
        callback.from_user.id,
        Config.texts["ADMIN"]["ADD_WORD"]["ENTER"]
    )
