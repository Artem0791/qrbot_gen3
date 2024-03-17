from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router(name=__name__)


@router.callback_query(F.text == 'info')
async def create_callback(callback: CallbackQuery):
    await callback.answer(text="Please put your data in the text window and send it to me")
