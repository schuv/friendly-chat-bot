import functools

from aiogram.types import Message
from config import Config


class AdminMethods:
    """
    Different administrator methods
    """

    @staticmethod
    def check_admin() -> callable:
        """
        Decorator to check if wrote user is admin

        :params: First argument in decorated function
        must be ```Message``` or ```CallbackQuery```
        """

        def wrapper(func) -> callable:
            @functools.wraps(func)
            async def wrapped(*args, **kwargs) -> callable:
                message: Message = args[0]

                if str(message.from_user.id) not in Config.admins:
                    await message.answer(
                        text=Config.texts["ADMIN"]["ACCESS_DENIED"]
                    )
                    return

                return await func(*args, **kwargs)
            return wrapped
        return wrapper
