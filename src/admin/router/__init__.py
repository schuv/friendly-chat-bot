from aiogram import Router

from admin.router import (
    callbacks,
    messages
)


router = Router(name="Administrator router")
router.include_router(callbacks.router)
router.include_router(messages.router)
