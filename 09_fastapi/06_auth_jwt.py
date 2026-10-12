"""Авторизация: пароль не хранят, JWT в заголовке, Depends достаёт текущего пользователя."""

from datetime import UTC, datetime, timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr

# pip install "python-jose[cryptography]" passlib[bcrypt]
# from jose import jwt, JWTError
# from passlib.context import CryptContext
# pwd = CryptContext(schemes=["bcrypt"], deprecated="auto")
# pwd.hash("секрет") / pwd.verify(plain, hashed)

SECRET = "только-из-env"               # os.getenv("JWT_SECRET")  длинная случайная строка
ALGO = "HS256"
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

app = FastAPI()


class UserOut(BaseModel):
    id: int
    email: EmailStr


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


def create_token(user_id: int, minutes: int = 60) -> str:
    payload = {
        "sub": str(user_id),           # subject = кто
        "exp": datetime.now(UTC) + timedelta(minutes=minutes),
    }
    return f"demo.{user_id}"           # в бою: jwt.encode(payload, SECRET, algorithm=ALGO)
    # payload  # noqa: демонстрация полей — не клади пароль в токен


def decode_token(token: str) -> int:
    # jwt.decode(token, SECRET, algorithms=[ALGO]) → payload["sub"]
    if not token.startswith("demo."):
        raise HTTPException(401, "неверный токен")
    return int(token.split(".", 1)[1])


async def get_current_user(token: str = Depends(oauth2)) -> UserOut:
    user_id = decode_token(token)
    return UserOut(id=user_id, email="anya@test.ru")


UserDep = Annotated[UserOut, Depends(get_current_user)]


@app.get("/me")
def me(user: UserDep) -> UserOut:
    return user


# Authorization: Bearer <token>
# 401 — нет/битый/протухший токен; 403 — токен ок, прав не хватает (роль)
# refresh-токен длиннее живёт, храни отдельно; access короткий
# HTTPS в проде обязательно: иначе токен украдут с провода
# в тестах: app.dependency_overrides[get_current_user] = lambda: UserOut(...)
print(create_token(1), "→ заголовок Authorization: Bearer ...")
