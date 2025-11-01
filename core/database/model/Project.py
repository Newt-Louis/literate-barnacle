from typing import Optional

from pydantic import BaseModel, Field, field_validator

class Project(BaseModel):
    id: Optional[int] = None
    project_name: Optional[str] = None
    language: Optional[str] = None
    project_path: Optional[str] = None
    app_port: Optional[int] = None
    domain: Optional[str] = None
    is_enabled: Optional[bool] = None

    class Config:
        extra = "ignore"