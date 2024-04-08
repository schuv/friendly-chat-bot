from aiogram.fsm.state import (
    State,
    StatesGroup
)


class AdminPanel(StatesGroup):
    """
    States in administrator panel
    """

    panel: State = State()
    new_word: State = State()
    check_word: State = State()
