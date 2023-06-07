from nonebot import logger
from nonebot.adapters.onebot.v11 import Bot
from nonebot.exception import ActionFailed


async def get_nickname_by_id(bot: Bot, *id_: str, raise_on_failed: bool = False) -> str:
    assert len(id_) >= 1, "At least one id must be provided"
    try:
        if len(id_) >= 2 and id_[1] is not None:
            user_info = await bot.get_group_member_info(group_id=int(id_[0]), user_id=int(id_[1]))
            return user_info["card"] or user_info["nickname"]
        else:
            user_info = await bot.get_stranger_info(user_id=int(id_[0]))
            return user_info["nickname"]
    except ActionFailed as e:
        if raise_on_failed:
            raise e
        else:
            err_msg = f"获取昵称失败 ActionFailed id_={', '.join(map(str, id_))} bot=<{bot.type} {bot.self_id}> " \
                      f"exception={e}"
            logger.warning(err_msg)
            return f"qq_{id_[0]}"


__all__ = ("get_nickname_by_id",)
