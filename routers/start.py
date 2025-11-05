from aiogram import Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext

from keybords.start import get_start_kb

router = Router()


@router.message(or_f(CommandStart() , F.text == "➡️ Назад"))
async def start(message: Message, state: FSMContext):
    await message.answer("Hello", reply_markup=get_start_kb())