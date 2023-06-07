from nonebot_plugin_get_nickname import FuncManagerFactory


def register(factory: FuncManagerFactory):
    try:
        from nonebot.adapters.onebot.v11 import Adapter
        from .onebot_v11 import get_nickname
        factory.register(Adapter.get_name(), "get_nickname", get_nickname)
    except ImportError:
        pass

    try:
        from nonebot.adapters.qqguild import Adapter
        from .qqguild import get_nickname
        factory.register(Adapter.get_name(), "get_nickname", get_nickname)
    except ImportError:
        pass

    try:
        from nonebot.adapters.kaiheila import Adapter
        from .kaiheila import get_nickname
        factory.register(Adapter.get_name(), "get_nickname", get_nickname)
    except ImportError:
        pass

    try:
        from nonebot.adapters.console import Adapter
        from .console import get_nickname
        factory.register(Adapter.get_name(), "get_nickname", get_nickname)
    except ImportError:
        pass
