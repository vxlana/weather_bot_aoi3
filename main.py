import asyncio
import os
from aiogram import Bot, types, Dispatcher
from dotenv import load_dotenv
from handlers.get_weather import get_weather_router

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher

dp.include_router(get_weather_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    asyncio.run(main())