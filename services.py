from .template_env import jinja_env
from .config import config


class PanelService:

    @staticmethod
    def render_text(text: str):
        t = jinja_env.get_template("shell_panel.html")
        background_url = config.static_dir.joinpath("images/rikka1.png")
        content = t.render(background_url=background_url, pre_content=text)
        return content

    @staticmethod
    def render_text_xterm(text: str, theme: str):
        t = jinja_env.get_template("xterm.html")
        background_url = config.static_dir.joinpath("images/rikka1.png")
        content = t.render(background_url=background_url, pre_content=text, theme=theme)
        return content
