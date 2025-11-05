from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from configs import TOKEN


properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML
)

bot = Bot(token=TOKEN, default=properties)
dp = Dispatcher()