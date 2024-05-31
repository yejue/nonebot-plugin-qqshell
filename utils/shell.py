import time
import paramiko


class ShellSync:
    """同步 SSH Shell 类"""

    def __init__(self, hostname: str, port: int, username: str, password: str):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

        self.ssh_client, self.shell = self.set_shell()
        self.panel = self.set_panel()

        if self.is_connect():
            self.on_recv()

    def set_shell(self):
        ssh = paramiko.SSHClient()

        try:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.hostname, self.port, self.username, self.password)
            shell = ssh.invoke_shell()
            print(f"Shell: {id(shell)} 连接")
        except Exception as e:
            print(e)
            ssh.close()
            return None, None
        return ssh, shell

    @staticmethod
    def set_panel():
        """输出面板"""
        return ""

    def exec_command(self, command: str):
        """执行命令"""
        cmd_template = f"{command}\r"
        self.shell.send(cmd_template.encode())
        self.panel += cmd_template
        self.on_recv()

    def on_recv(self, size: int = 32 * 1024, encoding: str = "utf8"):
        """接收返回"""
        time.sleep(0.5)
        output = ""
        while self.shell.recv_ready():
            data = self.shell.recv(size).decode(encoding)
            output += data
        self.panel += output

    def get_standard_panel_text(self, row_num: int = 48):
        """按照行宽和列宽获取标准面板"""
        output = self.get_output()
        output_list = output.split("\r\n")[-row_num:]
        text = "\r\n".join(output_list)
        return text

    def get_output(self):
        return self.panel.replace('\r', '\\r').replace('\n', '\\n').replace('"', '\\"').replace("'", "\\'")

    def is_connect(self):
        if not self.ssh_client:
            return False
        transport = self.ssh_client.get_transport()
        if transport is not None and transport.is_active():
            return True
        return False

    def close(self):
        if self.ssh_client:
            self.ssh_client.close()
