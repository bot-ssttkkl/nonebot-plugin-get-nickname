nonebot-plugin-get-nickname
====

为不同平台提供通用方法获取用户昵称

## 用法

```python
from nonebot_plugin_get_nickname import get_nickname, get_bot_nickname

nickname = get_nickname(event, bot)
bot_nickname = get_bot_nickname(bot)
```

## 支持的 adapter

| OneBot v11 | OneBot v12 | Console | Kaiheila | QQ Guild | Telegram |
|:----------:|:----------:|:-------:|:--------:|:--------:|:--------:|
|     ✅      |            |         |          |    ✅     |          |
