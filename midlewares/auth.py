from typing import Callable, Any, Dict, Awaitable, Union

from services.user_menager import UserMenager

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class AuthMiddleware(BaseMiddleware):
    async def __call__(
        self,

        handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:
        manager = UserMenager()
        user = manager.get(obj_id=event.from_user.id)
        if not user:
            manager.create(id=event.from_user.id, fullname=event.from_user.full_name,
                           language=event.from_user.language_code)
            user = manager.get(obj_id=event.from_user.id)
        data["user"] = user
        return await handler(event, data)
