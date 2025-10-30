from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Начать", callback_data="start"),
            InlineKeyboardButton(text="👤 Профиль", callback_data="profile"),
        ]
    ]
)