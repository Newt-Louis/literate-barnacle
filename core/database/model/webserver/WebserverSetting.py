import sqlite3
from core.config import config
from typing import Optional

class WebserverSetting:
    DB_PATH = config.DB_PATH
    def __init__(self, server_name: str,
                 id: Optional[int] = None,
                 selected_version: Optional[str] = None,
                 executable_path: Optional[str] = None,
                 sites_enabled_path: Optional[str] = None,
                 tld_template: str = '.test',
                 http_port: Optional[int] = None,
                 ssl_port: Optional[int] = None,
                 alp_path: Optional[str] = None,  # Access Log Path
                 elp_path: Optional[str] = None,  # Error Log Path
                 is_enabled: int = 0,
                 **kwargs):
        self.id = id
        self.server_name = server_name
        self.selected_version = selected_version
        self.executable_path = executable_path
        self.sites_enabled_path = sites_enabled_path
        self.tld_template = tld_template
        self.http_port = http_port
        self.ssl_port = ssl_port
        self.alp_path = alp_path
        self.elp_path = elp_path
        self.is_enabled = bool(is_enabled)

    def __repr__(self):
        return (f"<WebserverSetting(id={self.id}, "
                f"name='{self.server_name}', "
                f"version='{self.selected_version}')>")