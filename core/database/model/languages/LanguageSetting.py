from pydantic import BaseModel, Field, field_validator
from typing import Optional

class LanguageSetting(BaseModel):
    id: Optional[int] = None
    language: str
    selected_version: str
    executable_path: str
    root_folder: str
    is_ssl_enabled: bool = Field(default=False)
    is_chosen: bool = Field(default=False)

    class Config:
        extra = "ignore"