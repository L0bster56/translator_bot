from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.utils.i18n import FSMI18nMiddleware
from aiogram.client.default import DefaultBotProperties

from configs import TOKEN, i18n

from routes.start import router as start_handler
from routes.about import router as about_handler
from routes.settings import router as settings_handler
from routes.translate import router as translate_handler
from routes.trans_history import router as trans_history_handler

properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML,
)

bot = Bot(TOKEN, default=properties)
dp = Dispatcher()

dp.message.middleware(FSMI18nMiddleware(i18n))
dp.include_router(start_handler)
dp.include_router(about_handler)
dp.include_router(settings_handler)
dp.include_router(translate_handler)
dp.include_router(trans_history_handler)
