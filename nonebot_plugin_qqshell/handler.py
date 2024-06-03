from nonebot.rule import to_me
from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters import Message, MessageSegment
from nonebot.log import logger
from nonebot.permission import SUPERUSER
from nonebot_plugin_htmlrender import html_to_pic
from nonebot.adapters.onebot.v11 import MessageSegment


from .services import PanelService
from .config import config
from .utils.shell import ShellSync


def get_shell():

    host_dict = {
        "hostname": config.qqshell_host,
        "port": config.qqshell_port,
        "username": config.qqshell_host_user,
        "password": config.qqshell_host_password,
    }
    print(host_dict)

    _shell = ShellSync(**host_dict)
    return _shell


shell = get_shell()
qq_shell = on_command(
    "shell",
    aliases={
        ">shell",
    },
    rule=to_me(),
    permission=SUPERUSER,
    priority=config.qqshell_priority,
    block=True,
)


@qq_shell.handle()
async def shell_handler(args: Message = CommandArg()):
    command = "" if not args else args.extract_plain_text()

    # 命令执行并获取结果
    if shell.is_connect():
        shell.exec_command(command)
    else:
        logger.error("Shell 连接失败，请确认连接配置")
        return

    res = shell.get_output()

    # 输出结果
    pic = await html_to_pic(
        PanelService.render_text_xterm(text=res, theme=config.qqshell_theme)
    )
    message = MessageSegment.image(file=pic)
    await qq_shell.finish(message)
