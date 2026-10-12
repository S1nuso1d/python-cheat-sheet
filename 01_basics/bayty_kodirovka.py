"""Байты и кодировки. str — текст (символы), bytes — сырые байты. Связка: encode / decode."""

# файл, сеть, БД — это байты. Python str внутри — Unicode.
# utf-8: один символ = 1..4 байта; латиница 1, кириллица 2, эмодзи 4

text = "Привет"
raw = text.encode("utf-8")
print(raw)                             # b'\xd0\x9f...'  префикс b = bytes
print(raw.decode("utf-8"))             # Привет

# decode не той кодировкой → кракозябры или UnicodeDecodeError
# Windows-файлы старые часто cp1251; веб и Linux — utf-8
try:
    raw.decode("ascii")
except UnicodeDecodeError as e:
    print("ascii не тянет кириллицу:", type(e).__name__)

# ошибки: errors="replace" → � ; "ignore" теряет данные; по умолчанию "strict"
print(b"\xff".decode("utf-8", errors="replace"))

print(len("ё"), len("ё".encode()))     # 1 символ, 2 байта
print(list("аб"))                      # ['а', 'б']  не байты

# открывать текстовые файлы с encoding="utf-8"
# бинарные (картинка, zip): open(..., "rb") / Path.read_bytes()
# BOM в Excel: encoding="utf-8-sig"
# никогда не мешай str и bytes: "a" + b"b" → TypeError
