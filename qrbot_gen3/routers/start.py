from aiogram import Bot, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.markdown import hbold

from qrbot_gen3.logger import logger

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message):
    logger.info(f"User {message.from_user.id} launched bot")
    button = [[InlineKeyboardButton(text="Create", callback_data="create_qr")]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}!\nPress 'Create' to generate a QR code.",
                         reply_markup=keyboard)

