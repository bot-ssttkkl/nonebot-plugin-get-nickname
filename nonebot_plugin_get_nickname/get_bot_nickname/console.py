from nonebot.adapters.console import Bot


async def get_bot_nickname(bot: Bot, *, raise_on_failed: bool = False) -> str:
    return "Bot"


__all__ = ("get_bot_nickname",)
