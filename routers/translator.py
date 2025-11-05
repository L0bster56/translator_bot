from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from pyexpat.errors import messages

from keybords.start import get_start_kb
from keybords.translator import lang_kb_f
from servises.translator import translate

router = Router()
text = ""
src = ""
dest = ""

@router.message(F.text == "🔍 Перевод")
async def lang_f(message: Message):
    await message.answer("С какого языка?", reply_markup=lang_kb_f())

@router.message(F.text == "en: 🇺🇸")
async def send_kb_f(message: Message):
    await message.answer("Ведите текст: ")
    dest = "en"



@router.message(F.text == "ru: 🇷🇺")
async def send_kb_l(message: Message):
    src = "ru"
    await message.answer(translate(text, src, dest))
    await message.answer("Всё", reply_markup=get_start_kb())


@router.message(F.text)
async def lang_l(message: Message):
    await message.answer("На какой язык перевести", reply_markup=lang_kb_f())
    text = message.text



