from typing import Optional
from pydantic import BaseModel, Field, field_validator

class WebserverSetting(BaseModel):
    id: Optional[int] = None
    server_name: str
    selected_version: Optional[str] = None
    executable_path: Optional[str] = None
    sites_enabled_path: Optional[str] = None
    tld_template: str = Field(default=".test")
    http_port: Optional[int] = None,
    ssl_port: Optional[int] = None,
    alp_path: Optional[str] = None,  # Access Log Path
    elp_path: Optional[str] = None,  # Error Log Path
    is_enabled: bool = Field(default=False)

    class Config:
        extra = "ignore"

    @field_validator('is_enabled', mode='before')
    @classmethod
    def convert_int_to_bool(cls, v: any) -> bool:
        # Nếu đầu vào là int (0 hoặc 1 từ DB), nó sẽ chuyển thành bool
        if isinstance(v, int):
            return bool(v)
        return v