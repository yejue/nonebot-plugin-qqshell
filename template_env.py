from jinja2 import Environment, FileSystemLoader

from .config import config


def create_jinja2_env():
    """创建 Jinja2 环境"""
    env = Environment(loader=FileSystemLoader(config.template_dir))
    return env


jinja_env = create_jinja2_env()
