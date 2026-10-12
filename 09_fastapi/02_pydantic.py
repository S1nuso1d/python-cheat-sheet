"""Pydantic — схемы входа/выхода. FastAPI из типов делает валидацию и /docs."""

from pydantic import BaseModel, Field, EmailStr, field_validator


class TaskCreate(BaseModel):                 # то, что ПРИНИМАЕМ
    title: str = Field(min_length=1, max_length=200)
    priority: str = Field(default="mid", pattern="^(low|mid|high)$")


class TaskOut(TaskCreate):                   # то, что ОТДАЁМ
    id: int
    done: bool = False


class UserCreate(BaseModel):
    email: EmailStr                          # pip: email-validator
    age: int = Field(ge=0, le=120)
    password: str = Field(min_length=8)

    @field_validator("password")
    @classmethod
    def strong(cls, v: str) -> str:
        if not any(c.isdigit() for c in v) or not any(c.isupper() for c in v):
            raise ValueError("нужны цифра и заглавная")
        return v


class UserOut(BaseModel):                    # пароль сюда НЕ кладём
    id: int
    email: EmailStr


# разделение Create / Update / Out — правило: наружу не светить секреты
# Update: все поля Optional, потом model_dump(exclude_unset=True) для PATCH

payload = TaskCreate(title="хлеб")
print(payload.model_dump())                  # dict
print(TaskOut(id=1, **payload.model_dump()))

# невалидное → ValidationError (в API это 422)
try:
    TaskCreate(title="")
except Exception as e:
    print(type(e).__name__)

# SQLAlchemy-модель ≠ схема. Связка: model_config = ConfigDict(from_attributes=True)
# pydantic-settings: настройки из .env  class Settings(BaseSettings): db_url: str
