"""Файлы: with сам закроет. Всегда encoding='utf-8'. Пути — pathlib."""

from pathlib import Path
import json

# режимы: r чтение  w перезапись (создаёт)  a дописать  x создать или ошибка  b двоичный
# with — даже при ошибке внутри файл закроется

demo = Path("cheat_demo.txt")
with demo.open("w", encoding="utf-8") as f:
    f.write("первая\n")                # write сам \n НЕ ставит
    f.writelines(["вторая\n", "третья\n"])

with demo.open("r", encoding="utf-8") as f:
    for line in f:                     # построчно, мало памяти
        print(repr(line))              # 'первая\n'  — снимай rstrip()
# f.read()      всё одной строкой
# f.readlines() список строк

# pathlib
p = Path("data") / "notes.txt"         # / собирает путь и на Windows, и на Linux
print(p.name, p.suffix, p.stem)        # notes.txt  .txt  notes
# p.exists(), p.mkdir(exist_ok=True), Path(".").glob("*.py")
# p.read_text(encoding="utf-8")
# p.write_text("текст", encoding="utf-8")
# Path(__file__).parent  — папка ЭТОГО файла (не текущая рабочая)

# JSON — словарь/список ↔ текст
data = {"name": "Аня", "ok": True, "n": None}
text = json.dumps(data, ensure_ascii=False, indent=2)  # False = русский как есть
print(text)
print(json.loads(text))
# json.dump(obj, file) / json.load(file)

demo.unlink(missing_ok=True)           # убрать учебный файл

# FileNotFoundError — нет файла в режиме r
# без utf-8 на Windows русский → кракозябры или UnicodeDecodeError
# даты в JSON сами не пишутся: dt.isoformat()
