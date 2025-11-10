import os

from aiogram.utils.i18n import I18n

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")

# I18n -> internalization
i18n = I18n(path="locales", domain="messages")

# Функция для перевода
_ = i18n.gettext
