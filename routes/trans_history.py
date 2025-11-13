from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from states.translate import TransForm

from keyboards.translate import get_from_lang_kb, get_to_lang_kb
from keyboards.start import get_back_kb, get_start_kb

from services.translate import translate

from services.history import HistoryMenager

from configs import __, _

menager = HistoryMenager()

router = Router()


@router.message(F.text.in_(__("📚 история")) )
async def translate_handler(message: Message, user: dict):
    texts = f"{message.from_user.first_name}:\n\n"
    lists = menager.list(user_id=message.from_user.id)

    print(lists)

    for item in lists:
        texts += f"{item['src']} → {item['dest']} | {item['text']} = {item['trans_text']}\n"
    if len(lists) <= 0:
        await message.answer(
            _("У вас истории нету", locale=user.get("lang"))
        )
        return
    await message.answer(texts)
