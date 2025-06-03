import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardMarkup, KeyboardButton, WebAppInfo, InlineKeyboardButton

dp = Dispatcher()
TOKEN = '7855490726:AAEORGnqjbE8N4dC5XuwmzoDkP7y_Fh6SEc'

@dp.message(CommandStart)
async def command_pizza_handler(message: Message) -> None:
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
          [
              InlineKeyboardButton(
                  text="Перейти к медитации",
                  web_app=WebAppInfo(url=f'https://deltaopensourc.github.io/Meditation/'),
              )
          ]  
        ]  
    )
    await message.answer(text='Медитация', reply_markup=markup)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())