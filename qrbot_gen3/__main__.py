import asyncio
import logging
from contextlib import suppress

from aiogram import Bot
from aiogram.enums import ParseMode

from config_reader import config
from dispatcher import init_dispatcher


async def start_bot(token: str):
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = init_dispatcher()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def main():
    await start_bot(token=config.bot_token.get_secret_value())

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
