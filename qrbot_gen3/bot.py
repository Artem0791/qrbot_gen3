import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, FSInputFile
from aiogram.utils.markdown import hbold
import qrcode
from config import Config, QRCodeConfig, UserMessage

from pydantic import ValidationError

config = Config()
qr_config = QRCodeConfig

bot = Bot(token=config.bot_token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    button = [[InlineKeyboardButton(text="Create", callback_data="create_qr")]]
    keyboard = InlineKeyboardMarkup(inline_keyboard=button)
    await message.answer(text=f"Hello, {hbold(message.from_user.full_name)}!\nPress 'Create' to generate a QR code.",
                         reply_markup=keyboard)


@dp.callback_query()
async def handle_create(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Enter URL for QR code generation:", reply_markup=None)


@dp.message()
async def text_to_qr(message: Message):
    try:
        user_message = UserMessage(url=message.text)
        await message.answer("Received valid URL.")
        # не работает, ошибка version=qr_config.version <--
        # qr = qrcode.QRCode(version=qr_config.version,
        #                    error_correction=qrcode.constants.ERROR_CORRECT_L,
        #                    box_size=qr_config.box_size,
        #                    border=qr_config.box_size)

        qr = qrcode.QRCode(version=1,
                           error_correction=qrcode.constants.ERROR_CORRECT_L,
                           box_size=20,
                           border=2)

        qr.add_data(user_message)
        qr.make(fit=True)

        img = qr.make_image(fill_color='black', back_color='white')
        img.save('qr_code.png')
        photo_path = r'qr_code.png'
        await message.reply_photo(photo=FSInputFile(path=photo_path), caption="Your QR is ready!", parse_mode='HTML')
    except ValidationError:
        await message.answer(f"Please send a valid URL.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

