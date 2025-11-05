import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import CommandStart, Command
from bot import bot, dp

from bs4 import BeautifulSoup
import requests



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())