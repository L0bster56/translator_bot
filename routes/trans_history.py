from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from states.translate import TransForm

from keyboards.translate import get_from_lang_kb,get_to_lang_kb
from keyboards.start import get_back_kb, get_start_kb

from services.translate import translate

from services.history import HistoryMenager



menager = HistoryMenager()

router = Router()

@router.message(F.text == "📚 история")
async def translate_handler(message: Message):
    text = f"История поиска {message.from_user.first_name}"
    lists = menager.list(user_id=message.from_user.id)
    print(lists)
    for text in lists:
        text += f"\n{text.src} <-> {text.text} == {text.trans_text} <-> {text.dest}"
    await message.answer(text)