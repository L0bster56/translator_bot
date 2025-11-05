from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from configs import TOKEN
from routers.start import router as start_router
from routers.translator import router as translator_router


properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML
)

bot = Bot(token=TOKEN, default=properties)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(translator_router)