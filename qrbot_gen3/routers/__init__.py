from aiogram import Dispatcher

from . import start


routers = [start.router]


def register_router(dp: Dispatcher):
    dp.include_routers(*routers)
