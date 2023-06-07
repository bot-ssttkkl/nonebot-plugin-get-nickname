from typing import Union

from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11.event import Sender
from nonebot_plugin_session import Session, extract_session

from ..get_nickname_by_id.kaiheila import get_nickname_by_id


async def get_nickname(session_or_event: Union[Session, Event], bot: Bot, *, raise_on_failed: bool = False) -> str:
    if isinstance(session_or_event, Event):
        sender: Sender = getattr(session_or_event, "sender", None)
        if sender is not None and sender.nickname is not None:
            return sender.nickname

        session = extract_session(bot, session_or_event)
    else:
        session = session_or_event

    return await get_nickname_by_id(bot, session.id1, session.id2, session.id3, raise_on_failed=raise_on_failed)


__all__ = ("get_nickname",)
