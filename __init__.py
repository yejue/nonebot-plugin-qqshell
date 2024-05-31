from nonebot import require
require("nonebot_plugin_htmlrender")

from nonebot.plugin import PluginMetadata
from .config import Config
from .handler import shell_handler

__plugin_meta__ = PluginMetadata(
    name="QQShell: 执行任何你所能想到的命令",
    description=(
        "QQShell 能执行任何你所能想到的服务器命令\n"
        "   >shell cd /\n"
        "   >shell pwd\n"
        "   >shell su\n"
    ),
    usage=">shell 你的指令",
    config=Config,
)
