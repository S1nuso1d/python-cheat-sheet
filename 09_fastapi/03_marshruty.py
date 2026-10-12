"""
FastAPI: маршруты. Это справочник — чтобы запустить сервер:

    pip install fastapi uvicorn
    uvicorn 09_fastapi.03_marshruty:app --reload
    открыть http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI, HTTPException, Query, Path, status

app = FastAPI(title="Tasks API", version="1.0.0")

# как FastAPI понимает, откуда параметр:
#   есть в пути /tasks/{id}     → path
#   простой тип, не в пути      → query  (?limit=20)
#   Pydantic-модель             → JSON-тело


@app.get("/ping")
def ping():
    return {"status": "ok"}                  # dict → JSON сам


@app.get("/echo/{text}")
def echo(text: str):
    return {"text": text}


@app.get("/sum")
def add(a: int, b: int = 0):                 # query: /sum?a=2&b=3
    return {"result": a + b}


tasks: dict[int, dict] = {}


@app.get("/tasks")
def list_tasks(
    done: bool | None = None,
    limit: int = Query(20, ge=1, le=100),    # валидация query
):
    items = list(tasks.values())
    if done is not None:
        items = [t for t in items if t["done"] is done]
    return items[:limit]


@app.get("/tasks/{task_id}")
def get_task(task_id: int = Path(gt=0)):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="не найдено")
    return tasks[task_id]


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(title: str):
    new_id = max(tasks, default=0) + 1
    tasks[new_id] = {"id": new_id, "title": title, "done": False}
    return tasks[new_id]


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(404, "не найдено")
    del tasks[task_id]
    return None                              # 204 без тела

# def vs async def:
#   обычный def FastAPI крутит в пуле потоков — ок для sync-кода
#   async def + блокирующий requests.get / time.sleep — СТОПОРИТ весь сервер
#   в async используй httpx.AsyncClient, asyncio.sleep, AsyncSession

# APIRouter: вынести группу в файл, затем app.include_router(router, prefix="/api/v1")
# response_model=TaskOut  отфильтрует лишние поля (пароль не уйдёт)
