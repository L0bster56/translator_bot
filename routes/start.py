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
async def start_handler(message: Message, state: FSMContext):
    user = manager.get(obj_id=message.from_user.id)
    if user is None:
        manager.create(id=message.from_user.id, fullname=message.from_user.full_name, language=message.from_user.language_code)
    await state.clear()
    await message.answer("hello", reply_markup=get_start_kb())
