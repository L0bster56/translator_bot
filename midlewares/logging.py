from typing import Callable, Any, Dict, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,

        handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:

        print(data)

        return await handler(event, data)
