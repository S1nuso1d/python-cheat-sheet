"""Сеть (requests) и регулярки (re). timeout обязателен. HTML regex'ом не парсят."""

import re

# requests (pip install requests)
# resp = requests.get(url, params={"q": "python"}, timeout=10)
# resp.raise_for_status()          # 4xx/5xx → исключение
# data = resp.json()
# POST: requests.post(url, json={"title": "хлеб"}, headers={"Authorization": f"Bearer {token}"})
# токен из os.getenv, не из кода
# Session() если много запросов; retry на 429/5xx

# --- regex ---
# r"..." raw-строка, иначе \d сломается
# . любой символ   \d цифра   \w буква/цифра/_   \s пробел
# * 0+  + 1+  ? 0|1   {2,5} от 2 до 5
# ^ начало  $ конец   [...] класс   | или   (...) группа

text = "лог 2026-09-12 ERROR диск"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
print(m.group(0), m.group(1))              # 2026-09-12  2026

pat = re.compile(r"(?P<level>ERROR|INFO) (?P<msg>.+)")
m = pat.search("ERROR диск полон")
print(m["level"], m["msg"])

print(re.findall(r"\d+", "a1 b23"))        # ['1', '23']
print(re.sub(r"\d", "*", "карта 1234"))    # карта ****
print(bool(re.fullmatch(r"[\w.-]+@.+\..+", "a@b.ru")))  # упрощённый email

# search — первое; match — только с начала; fullmatch — вся строка
# findall / finditer; sub замена; split
# жадность: .* берёт максимум, .*? минимум
# HTML/JSON регулярками не разбирают — bs4 / json.loads
# отладка шаблона: regex101.com  язык Python
