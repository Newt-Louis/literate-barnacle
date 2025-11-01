from pydantic import BaseModel, Field, field_validator
from typing import Optional

class LanguageSetting(BaseModel):
    id: Optional[int] = None
    language: str
    selected_version: str
    executable_path: Optional[str] = None
    root_folder: Optional[str] = None
    is_ssl_enabled: bool = Field(default=False)
    is_chosen: bool = Field(default=False)

    class Config:
        extra = "ignore"