from aiogram import Dispatcher

from routers import register_router


def init_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    register_router(dp)
    return dp
