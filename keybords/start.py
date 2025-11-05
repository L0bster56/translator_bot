from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_kb(leng: str = "ru"):
    bilder = ReplyKeyboardBuilder()
    bilder.button(text="🔍 Перевод")
    bilder.button(text="🧏🏿‍♂️ О нас")
    bilder.button(text="👨🏿‍🦯️ История поиск")

    bilder.adjust(1,2)

    return bilder.as_markup(resize_keyboard=True)