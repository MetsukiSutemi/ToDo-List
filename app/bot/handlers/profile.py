from aiogram import Router, types, F
from app.service import get_profiles_by_user

router = Router()

@router.callback_query(F.data == "profile")
async def profile_callback(callback: types.CallbackQuery):
    # ответить на инлайн-кнопку
    await callback.message.answer("Профиль")