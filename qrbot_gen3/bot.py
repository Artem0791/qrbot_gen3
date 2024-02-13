from aiogram import Bot, Dispatcher
from aiogram.types import Message, CallbackQuery, FSInputFile
import qrcode
from config import Config
from qrbot_gen3.logger import logger
from qrbot_gen3.types import QRCode, UserMessage

from pydantic import ValidationError

config = Config()

bot = Bot(token=config.tg.bot_token, parse_mode="HTML")
dp = Dispatcher()


@dp.callback_query()
async def handle_create(callback_query: CallbackQuery):
    await callback_query.message.edit_text("Enter URL for QR code generation:", reply_markup=None)


@dp.message()
async def text_to_qr(message: Message):
    try:
        user_message = UserMessage(url=message.text)
        logger.info(f"Received message by {message.from_user.id}: {message.text}")
        await message.answer("Received valid URL.")

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
        await message.answer("Please send a valid URL.")
