from aiogram import Router, types, F
from app.bot.keyboards.start import start_keyboard
router = Router()

@router.message(F.text == "/start")
async def start_handler(message: types.Message):
    await message.answer("Добро пожаловать!",reply_markup=start_keyboard)