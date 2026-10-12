"""Модуль = файл .py. Пакет = папка с модулями. pip ставит чужие пакеты."""

import math                            # стандартная библиотека
import random as rnd                   # переименовать при импорте
from datetime import date, timedelta   # конкретные имена
# from math import *                   # плохо: не видно, откуда имена

print(math.sqrt(9), rnd.randint(1, 6), date.today())

# свой файл utils.py  →  import utils  /  from utils import bmi
# if __name__ == "__main__":
#     main()
# при запуске файла __name__ == "__main__"
# при import __name__ == "имя_модуля"  — блок main не выполнится

# НЕ называй файл random.py / json.py — перекроешь библиотеку (ModuleNotFoundError сюрприз)

# pip (в виртуальном окружении!):
#   python -m venv .venv
#   .venv\Scripts\activate
#   pip install fastapi uvicorn pytest httpx
#   pip freeze > requirements.txt
#   pip install -r requirements.txt
# .venv и .env НЕ коммитят в git

print("__name__ этого файла:", __name__)
if __name__ == "__main__":
    print("запустили напрямую, не через import")
