from typing import Union

from nonebot.adapters.console import Bot, Event
from nonebot_plugin_session import Session


async def get_nickname(session_or_event: Union[Session, Event], bot: Bot, *, raise_on_failed: bool = False) -> str:
    return "User"


__all__ = ("get_nickname",)
