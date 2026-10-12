"""JSON и CSV — как данные ездят между программами. Кодировка utf-8 всегда."""

import json
import csv
from pathlib import Path

data = {"name": "Аня", "skills": ["python", "sql"], "ok": True, "n": None}
text = json.dumps(data, ensure_ascii=False, indent=2)
print(text)
print(json.loads(text))

# dump/load — сразу в файл; dumps/loads — строка
# True/False/None ↔ true/false/null
# даты, set, объект класса сами не сериализуются: date.isoformat(), Enum.value

tmp = Path("_demo.csv")
rows = [{"name": "хлеб", "price": "50"}, {"name": "чай", "price": "80"}]
with tmp.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["name", "price"])
    w.writeheader()
    w.writerows(rows)

with tmp.open(encoding="utf-8") as f:
    for row in csv.DictReader(f):          # значения ВСЕГДА строки
        print(row["name"], int(row["price"]))

tmp.unlink()

# Excel часто хочет utf-8-sig; старые файлы — cp1251
# split(",") ломается на "Москва, РФ" в кавычках — поэтому модуль csv
# YAML конфиги: yaml.safe_load (не load)
