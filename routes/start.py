from aiogram import Router, F
from aiogram.filters import or_f
from aiogram.filters.command import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.start import get_start_kb
from services.user_menager import UserMenager

router = Router()
manager = UserMenager()

@router.message(or_f(CommandStart(), F.text == "⏪ назад"))
async def start_handler(message: Message, state: FSMContext, user: dict):
    print(user)
    await state.clear()
    await message.answer("hello", reply_markup=get_start_kb(user.get("language")))
