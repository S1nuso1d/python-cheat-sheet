"""Тесты FastAPI без живого сервера. pytest 09_fastapi/test_api.py -v"""

from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient

app = FastAPI()
_store: dict[int, dict] = {}


@app.post("/tasks", status_code=201)
def create(title: str):
    i = max(_store, default=0) + 1
    _store[i] = {"id": i, "title": title}
    return _store[i]


@app.get("/tasks/{i}")
def get_one(i: int):
    if i not in _store:
        raise HTTPException(404, "нет")
    return _store[i]


client = TestClient(app)


def test_create_and_get():
    _store.clear()
    r = client.post("/tasks", params={"title": "хлеб"})
    assert r.status_code == 201
    task_id = r.json()["id"]
    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "хлеб"


def test_missing():
    _store.clear()
    assert client.get("/tasks/999").status_code == 404


# JSON-тело: client.post("/tasks", json={"title": "хлеб"})
# подмена Depends: app.dependency_overrides[get_db] = lambda: fake_session
# внешний HTTP мокай (respx / unittest.mock) — тесты без интернета
# async: httpx.AsyncClient(transport=ASGITransport(app=app), base_url="http://t")
