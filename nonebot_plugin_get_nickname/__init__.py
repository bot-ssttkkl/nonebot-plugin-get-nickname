from nonebot import require

require("nonebot_plugin_session")

from nonebot.plugin import PluginMetadata

from .func_manager import FuncManager, FuncManagerFactory
from .get_bot_nickname import register as register_get_bot_nickname
from .get_nickname_by_id import register as register_get_nickname_by_id
from .get_nickname import register as register_get_nickname
from typing import Union

from nonebot import Bot
from nonebot.internal.adapter import Event
from nonebot_plugin_session import Session

func = FuncManagerFactory()
register_get_nickname(func)
register_get_bot_nickname(func)
register_get_nickname_by_id(func)

__plugin_meta__ = PluginMetadata(
    name="获取用户昵称",
    description="为不同平台提供通用方法获取用户昵称",
    usage="无",
    type="library",
    homepage="https://github.com/bot-ssttkkl/nonebot-plugin-get-nickname",
    supported_adapters={"~onebot.v11", "~qqguild", "~kaiheila"}
)


async def get_nickname_by_id(bot: Bot, *id_: str, raise_on_failed: bool = False) -> str:
    return await func(bot.type).get_nickname_by_id(bot, *id_, raise_on_failed=raise_on_failed)


async def get_bot_nickname(bot: Bot, *, raise_on_failed: bool = False) -> str:
    return await func(bot.type).get_bot_nickname(bot, raise_on_failed=raise_on_failed)


async def get_nickname(session_or_event: Union[Session, Event], bot: Bot, *, raise_on_failed: bool = False) -> str:
    return await func(bot.type).get_nickname(session_or_event, bot, raise_on_failed=raise_on_failed)
