"""logging и переменные окружения. print — для скрипта; лог — для сервиса."""

import logging
import os
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,                # DEBUG < INFO < WARNING < ERROR < CRITICAL
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
log = logging.getLogger("shop")        # имя модуля, не root

log.debug("мелочь, в проде обычно скрыта")
log.info("сервер слушает 8000")
log.warning("диск на 90%")
try:
    1 / 0
except ZeroDivisionError:
    log.exception("упали")             # трейсбэк в лог, не проглатывай молча

# logger на модуль: log = logging.getLogger(__name__)
# не логируй пароли и токены
# в FastAPI/uvicorn логи уже настроены — свой basicConfig может дублировать строки


# --- окружение ---
# секреты и URL не в код:  set API_TOKEN=...   /  .env + pydantic-settings
token = os.getenv("API_TOKEN", "")     # нет переменной → "" (или None если без default)
debug = os.getenv("DEBUG", "0") == "1"
print("token задан:" , bool(token), "debug:", debug)

# Path.home(), os.getcwd() — домашка и текущая папка процесса
print("cwd:", Path.cwd())
# .env НЕ коммитят; в git — .env.example с пустыми ключами
