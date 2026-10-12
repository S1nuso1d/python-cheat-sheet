"""APIRouter, настройки, CORS, lifespan. Большое приложение режут на пакеты, не держат всё в main."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic_settings import BaseSettings, SettingsConfigDict

# pip install fastapi uvicorn pydantic-settings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    app_name: str = "HealthApp"
    debug: bool = False
    cors_origins: str = "http://localhost:5173"   # в .env список через запятую
    # database_url: str                          без default = обязателен


settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # старт: пул БД, redis, прогрев
    app.state.ready = True
    yield
    # стоп: закрыть соединения
    app.state.ready = False


app = FastAPI(title=settings.app_name, lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",") if o.strip()],
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
def list_tasks():
    return []


@router.get("/{task_id}")
def get_task(task_id: int):
    raise HTTPException(404, "не найдено")


app.include_router(router, prefix="/api/v1")
# итоговые пути: GET /api/v1/tasks  и  GET /api/v1/tasks/{id}


@app.get("/health")
def health(x_request_id: str | None = Header(default=None)):
    return {"ok": True, "request_id": x_request_id}


# BackgroundTasks: @app.post(...) def create(..., bg: BackgroundTasks): bg.add_task(send_mail, email)
# статика/файлы: UploadFile, File(), Form() — multipart, не JSON
# кастомные ошибки: @app.exception_handler(MyError)
# версия API — prefix /api/v1, не ломай клиентов без новой версии
# несколько роутеров: users, tasks, auth — каждый файл = router
