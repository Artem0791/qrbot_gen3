from aiogram import Dispatcher

from . import start, create_qr, callback_answer


routers = [start.router, create_qr.router, callback_answer.router]


def register_router(dp: Dispatcher):
    dp.include_routers(*routers)
