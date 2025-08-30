import os.path
from kbds import keyboards
from aiogram import Router, types
from aiogram.filters import CommandStart

from kbds.keyboards import get_keyboard

get_weather_router = Router()



@get_weather_router.message(CommandStart())
async def welcome(message: types.Message):
    if not os.path.exists('user.txt'):
        open('user.txt', 'w').close()

    with open('user.txt', 'r') as joinedFile:
        joinedUsers = set(line.strip() for line in joinedFile)

        if str(message.chat.id) not in joinedUsers:
            with open('user.txt', 'a') as joinedFile:
                joinedFile.write(str(message.chat.id) + '\n')

    await message.bot.send_message(
        message.chat.id,
        f'Добро пожаловать, {message.from_user.first_name}! Какая погода вас интересует?',
        reply_markup=get_keyboard(
            "Погода на сегодня",
            "Погода на завтра",
            "Погода на неделю",
            "Настройки",
            "Поддержать разработчика",
            placeholder="Что вас интересует?",
            sizes=(2, 1, 2)
        )
    )

    await message.bot.send_message(
        message.chat.id,
        "Главное меню:",
        reply_markup=get_keyboard(
            "Погода на сегодня",
            "Погода на завтра",
            "Погода на неделю",
            "Настройки",
            "Поддержать разработчика",
            placeholder="Что вас интересует?",
            sizes=(2, 1, 2)
        )
    )

