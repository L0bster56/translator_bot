from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder



def lang_kb_f():
    builder = ReplyKeyboardBuilder()
    builder.button(text="en: 🇺🇸")
    builder.button(text="ru: 🇷🇺")
    builder.button(text="de: 🇩🇪")
    builder.button(text="ja: 🇯🇵")
    builder.button(text="fr: 🇫🇷")
    return builder.as_markup(resize_keyboard=True)



