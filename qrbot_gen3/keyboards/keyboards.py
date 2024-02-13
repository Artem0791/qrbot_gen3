from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button = [[InlineKeyboardButton(text="Create", callback_data="create_qr")]]
ikb = InlineKeyboardMarkup(inline_keyboard=button)
