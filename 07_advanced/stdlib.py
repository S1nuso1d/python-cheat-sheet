"""Стандартная библиотека: сначала ищи здесь, потом пиши своё."""

from collections import Counter, defaultdict, deque
from datetime import datetime, date, timedelta
from pathlib import Path

print(Counter("абракадабра").most_common(3))    # [('а', 5), ('б', 2), ('р', 2)]

groups = defaultdict(list)                      # нет ключа → сам создаст list()
for w in ["дом", "дуб", "кот"]:
    groups[w[0]].append(w)
print(dict(groups))                             # {'д': ['дом','дуб'], 'к': ['кот']}

q = deque([1, 2, 3])                            # быстрые pop/append с ОБОИХ концов
q.appendleft(0)
q.popleft()
# list.pop(0) медленный; deque.popleft() быстрый

now = datetime.now()
print(now.strftime("%d.%m.%Y %H:%M"))           # 12.10.2026 21:00
d = datetime.strptime("12.09.2026", "%d.%m.%Y").date()
print(d + timedelta(days=30), (d - date.today()).days)

# json: dumps/loads строка, dump/load файл; ensure_ascii=False
# random: choice, randint, shuffle, seed
# argparse: флаги CLI и --help
# logging вместо print в библиотечном коде (уровни DEBUG INFO WARNING ERROR)
# pathlib.Path — пути
print(Path(".").resolve())

# import this  — «Дзен Python»
# PEP 8: 4 пробела, snake_case, CamelCase классы, UPPER константы
