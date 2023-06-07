from nonebot import require
from nonebot.internal.matcher import Matcher

require("nonebot_plugin_get_nickname")

from nonebot.internal.adapter import Event
from nonebot import on_command, Bot

from nonebot_plugin_get_nickname import get_nickname, get_bot_nickname


@on_command("nickname").handle()
async def handle_get_nickname(matcher: Matcher, event: Event, bot: Bot):
    nickname = await get_nickname(event, bot, raise_on_failed=True)
    await matcher.send(nickname)


@on_command("bot_nickname").handle()
async def handle_get_bot_nickname(matcher: Matcher, bot: Bot):
    nickname = await get_bot_nickname(bot, raise_on_failed=True)
    await matcher.send(nickname)
