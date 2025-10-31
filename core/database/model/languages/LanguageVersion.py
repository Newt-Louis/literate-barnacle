from core.config import config
from typing import Optional

class LanguageVersion:
    def __init__(self, type: str, version: str, id: Optional[int] = None,
                 **kwargs):
        self.id = id
        self.type = type
        self.version = version

    def __repr__(self):
        return (f"<WebserverVersion(id={self.id}, "
                f"type='{self.type}', "
                f"version='{self.version}')>")