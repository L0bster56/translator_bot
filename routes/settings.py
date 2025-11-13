from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.start import get_back_kb
from keyboards.settings import get_lang_kb

from services.user_menager import UserMenager

manager = UserMenager()


from configs import __, _

router = Router()
@router.message(F.text.in_(__("⚙️ настройки")) )
async def send_welcome(message: Message, user: dict):
    await message.answer(_("настройки", locale=user.get("lang")), reply_markup=get_back_kb(user.get("lang")))
    await message.answer(_("выберите язык", locale=user.get("lang")), reply_markup=get_lang_kb())



@router.callback_query(F.data.startswith("lang"))
async def callback_lang(cb: CallbackQuery, user: dict):
    _, lang = cb.data.split("_")
    manager.update(user.get("id"), lang=lang)


