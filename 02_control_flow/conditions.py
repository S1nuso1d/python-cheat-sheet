"""if / elif / else. Проверки идут сверху вниз, стоп на ПЕРВОЙ истинной."""

age = 20
has_passport = True

if age >= 18 and has_passport:
    print("проход")
elif age >= 18:
    print("нужен паспорт")
else:
    print("молод")

# сравнение: == != < > <= >=     НЕ путать = (присвоить) и == (сравнить)
# логика:    and (оба)  or (хотя бы одно)  not (перевернуть)
# цепочка:   0 < x < 100     по-питоновски
# in:        answer in ("да", "yes", "y")

x = 7
print(x == 7, x != 8, 0 < x < 10)

# порядок важен: узкое условие ВЫШЕ широкого
total = 6000
if total > 5000:
    discount = 20
elif total > 1000:
    discount = 10
else:
    discount = 0
print("скидка", discount)          # 20  (если сначала >1000 — получилось бы 10)

# truthy / falsy: ложь — 0, 0.0, "", [], {}, None; остальное — истина
name = "Аня"
if name:                           # то же что if name != ""
    print("привет,", name)
print(bool("0"), bool("False"))    # True True  непустая строка!

# None сравнивают через is
result = None
if result is None:
    print("нет данных")

# ленивость: в a and b если a ложь — b не считают
n = 0
if n != 0 and 10 / n:              # деления не будет
    pass

# тернарный — выражение
status = "взрослый" if age >= 18 else "ребёнок"

# нормализуй ввод перед сравнением
# answer = input().strip().lower()
# if answer in ("да", "yes", "y", "д"):

# input() без int:  number = input(); number == 10  → всегда False ("10"!="10" wait, "10" == 10 is False yes)

# match/case (3.10+) вместо длинных elif по точному значению
op = "+"
match op:
    case "+":
        print(2 + 3)
    case "-":
        print(2 - 3)
    case _:
        print("неизвестно")
