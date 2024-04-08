from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Добавить новое слово",
                callback_data="NEW_WORD"
            ),
            InlineKeyboardButton(
                text="Проверить слово",
                callback_data="CHECK_WORD"
            )
        ]
    ]
)
