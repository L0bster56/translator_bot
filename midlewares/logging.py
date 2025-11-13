import logging

from typing import Callable, Any, Dict, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery


FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,

        handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:

        logger.info(
            f"{event.from_user.id} - {"MESSAGE" if isinstance(event, Message) else "Callback"} {event.from_user.first_name} {event.from_user.last_name}"
        )

        return await handler(event, data)
