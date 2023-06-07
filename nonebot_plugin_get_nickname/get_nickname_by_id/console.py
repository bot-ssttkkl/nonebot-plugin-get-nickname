from nonebot.adapters.console import Bot


async def get_nickname_by_id(bot: Bot, *id_: str, raise_on_failed: bool = False) -> str:
    return "User"


__all__ = ("get_nickname_by_id",)
