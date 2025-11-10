from aiogram.utils.keyboard import ReplyKeyboardBuilder

from configs import _


def get_start_kb(lang: str = "ru"):
    builder = ReplyKeyboardBuilder()
    builder.button(text=_("🔍 перевод", locale=lang))
    builder.button(text=_("👥 о нас", locale=lang))
    builder.button(text=_("📚 история", locale=lang))
    builder.button(text=_("⚙️ настройки", locale=lang))

    builder.adjust(1, 3)
    return builder.as_markup(resize_keyboard=True)


def get_back_kb(lang: str = "ru"):
    builder = ReplyKeyboardBuilder()
    builder.button(text=_("⏪ назад", locale=lang))
    return builder.as_markup(resize_keyboard=True)
