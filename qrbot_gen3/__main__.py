import asyncio
from contextlib import suppress

from aiogram import Bot
from aiogram.enums import ParseMode

from config import Config
from dispatcher import init_dispatcher

config = Config()


async def start_bot(token: str):
    bot = Bot(token=token, parse_mode=ParseMode.HTML)
    dp = init_dispatcher()
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


async def main():
    await start_bot(config.tg.bot_token)

if __name__ == "__main__":
    with suppress(KeyboardInterrupt, SystemExit):
        asyncio.run(main())
