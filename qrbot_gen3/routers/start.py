from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from qrbot_gen3.keyboards.start_keyboard import qr_inline_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}!\nPress 'Create' to generate a QR code.",
                         reply_markup=qr_inline_keyboard())

