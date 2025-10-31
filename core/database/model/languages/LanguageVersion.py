from core.config import config
from typing import Optional

class LanguageVersion:
    def __init__(self, type: str, versions: str, id: Optional[int] = None,
                 **kwargs):
        self.id = id
        self.type = type
        self.versions = versions

    def __repr__(self):
        return (f"<WebserverVersion(id={self.id}, "
                f"type='{self.type}', "
                f"version='{self.versions}')>")