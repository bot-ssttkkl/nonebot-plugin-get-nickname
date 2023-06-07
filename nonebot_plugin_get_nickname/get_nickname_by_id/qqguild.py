from nonebot import logger
from nonebot.adapters.qqguild import Bot
from nonebot.exception import ActionFailed


async def get_nickname_by_id(bot: Bot, *id_: str, raise_on_failed: bool = False) -> str:
    assert len(id_) >= 3, "At least three id must be provided"
    try:
        member = await bot.get_member(guild_id=id_[2], user_id=id_[0])
        return member.nick or f"qqguild_{id_[0]}"
    except ActionFailed as e:
        if raise_on_failed:
            raise e
        else:
            err_msg = f"获取昵称失败 ActionFailed id_={', '.join(map(str, id_))} bot=<{bot.type} {bot.self_id}> " \
                      f"exception={e}"
            logger.warning(err_msg)
            return f"qqguild_{id_[0]}"


__all__ = ("get_nickname_by_id",)
