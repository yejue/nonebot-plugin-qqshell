from pathlib import Path
from pydantic import BaseModel, Field
from nonebot import get_plugin_config


class Config(BaseModel):
    """Plugin Config Here"""
    qqshell_host: str = Field("localhost", doc="要连接的主机名")
    qqshell_port: int = Field(22, doc="要连接的主机 SSH 端口")
    qqshell_host_user: str = Field("root", doc="用户名")
    qqshell_host_password: str = Field("", doc="密码")
    qqshell_priority: int = Field(10, doc="QQShell 响应优先级")

    qqshell_theme: str = Field("theme_black_white_rikka", doc="Shell 主题")

    # 以下配置为插件默认配置
    base_dir: Path = Path(__file__).parent
    template_dir: Path = base_dir.joinpath("templates")
    static_dir: Path = base_dir.joinpath("static")


config = get_plugin_config(Config)