from nonebot import logger
from nonebot.adapters.kaiheila import Bot
from nonebot.adapters.kaiheila.api import User
from nonebot.exception import ActionFailed


async def get_nickname_by_id(bot: Bot, *id_: str, raise_on_failed: bool = False) -> str:
    assert len(id_) >= 1, "At least one id must be provided"
    user_id = id_[0]
    guild_id = id_[2] if len(id_) >= 3 else None
    try:
        user: User = await bot.user_view(user_id=user_id, guild_id=guild_id)
        return user.nickname or user.username or f"kaiheila_{user_id}"
    except ActionFailed as e:
        if raise_on_failed:
            raise e
        else:
            err_msg = f"获取昵称失败 ActionFailed id_={', '.join(map(str, id_))} bot=<{bot.type} {bot.self_id}> " \
                      f"exception={e}"
            logger.warning(err_msg)
            return f"kaiheila_{user_id}"


__all__ = ("get_nickname_by_id",)
