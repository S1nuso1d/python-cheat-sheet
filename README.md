# Шпаргалка: вся база Python + FastAPI + pytest

Открой папку темы → файл `.py` → читай комментарии справа.  
Запуск файла: `python путь\к\файлу.py` (из этой папки, с активированным `.venv`).

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Тесты:

```
pytest -v
pytest 08_pytest -v
pytest 09_fastapi/test_api.py -v
```

FastAPI-пример:

```
uvicorn 09_fastapi.03_marshruty:app --reload
# http://127.0.0.1:8000/docs
```

```
cheat_sheet_python/
├── 01_basics/          print, types, numbers, strings, bytes, == vs is
├── 02_control_flow/    if / match / while / for / range / zip
├── 03_collections/     list, tuple, dict, set, copies, unpacking
├── 04_functions/       def, *args, modules, lambda, closures
├── 05_errors_files/    except, files, JSON/CSV, logging, .env
├── 06_oop/             classes, dataclass, Enum, dunder, ABC
├── 07_advanced/        comprehensions, generators, decorators, typing, itertools
├── 08_pytest/          assert, fixtures, parametrize, marks, TestClient
├── 09_fastapi/         HTTP, Pydantic, routes, CRUD, Depends, JWT, SQLAlchemy
└── 10_sql_network/     SQL, sqlite3, requests, regex, async, datetime
```

Связанные темы лежат в одной папке. В каждом файле: зачем → примеры с комментариями → ловушки.

Порядок, если идёшь с нуля: `01` → `02` → `03` → `04` → `05` → `06` → `07` → `08` → `09` + `10`.
