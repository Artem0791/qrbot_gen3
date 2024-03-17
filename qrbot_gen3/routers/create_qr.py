from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from pydantic import ValidationError


from qrbot_gen3.misc.qr_generator import generate_qr
from qrbot_gen3.types import UserMessage

router = Router(name=__name__)


@router.message()
async def create_qr(message: Message):
    try:
        user_message = UserMessage(url=message.text)
        user_id = message.from_user.id
        user_name = message.from_user.first_name

        await message.answer("Received valid URL.")
        photo_path = generate_qr(user_message, user_id, user_name)
        await message.reply_photo(photo=FSInputFile(path=photo_path), caption="Your QR is ready!", parse_mode='HTML')
    except ValidationError:
        await message.answer("Please send a valid URL.")

