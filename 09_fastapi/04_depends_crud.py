"""Depends, слои, CRUD. Идея: эндпоинт тонкий, логика в сервисе, БД в репозитории."""

from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)


class TaskOut(TaskCreate):
    id: int
    done: bool = False


# «БД» в памяти — в проекте здесь Session SQLAlchemy
_db: dict[int, TaskOut] = {}


def get_db():
    """Зависимость. yield = закрыть сессию ПОСЛЕ ответа."""
    yield _db


Db = Annotated[dict[int, TaskOut], Depends(get_db)]


def pagination(page: int = 1, limit: int = 20) -> tuple[int, int]:
    return (page - 1) * limit, limit          # offset, limit


Page = Annotated[tuple[int, int], Depends(pagination)]


@app.post("/tasks", response_model=TaskOut, status_code=201)
def create(payload: TaskCreate, db: Db):
    new_id = max(db, default=0) + 1
    task = TaskOut(id=new_id, **payload.model_dump())
    db[new_id] = task
    return task


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(db: Db, page: Page, done: bool | None = None):
    offset, limit = page
    items = list(db.values())
    if done is not None:
        items = [t for t in items if t.done is done]
    return items[offset: offset + limit]


@app.patch("/tasks/{task_id}", response_model=TaskOut)
def patch_task(task_id: int, payload: TaskCreate, db: Db):
    if task_id not in db:
        raise HTTPException(404, "не найдено")
    data = payload.model_dump(exclude_unset=True)   # PATCH: только присланные поля
    old = db[task_id]
    db[task_id] = old.model_copy(update=data)
    return db[task_id]


# текущий пользователь — тоже Depends:
# async def get_current_user(token: str = Depends(oauth2)) -> User:
#     ... decode JWT ...
# UserDep = Annotated[User, Depends(get_current_user)]
# @app.get("/me")
# def me(user: UserDep): return user

# в тестах: app.dependency_overrides[get_db] = lambda: test_db
# CORSMiddleware для фронта; middleware логирует метод/путь/время
# списки ВСЕГДА с limit — иначе однажды вернёте миллион строк
# 409 на уникальный email: поймать IntegrityError → HTTPException(409)
