from aiogram import Bot, Dispatcher

from app.bot.handlers import start, profile  

bot = Bot("7740671025:AAEUlzfjcYKMJHfIvpFgx8VYqr98jnw2RQY")
dp = Dispatcher()
dp.include_router(start.router)
dp.include_router(profile.router)

async def start_bot():
    await dp.start_polling(bot)

