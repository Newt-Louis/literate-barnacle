from pydantic import BaseModel, Field, field_validator

class DashboardSetting(BaseModel):
    service: str
    type: str
    version: str
    is_running: bool = Field(default=False)

    class Config:
        extra = "ignore"

    @field_validator('is_running', mode='before')
    @classmethod
    def convert_int_to_bool(cls, v: any) -> bool:
        if isinstance(v, int):
            return bool(v)
        return v