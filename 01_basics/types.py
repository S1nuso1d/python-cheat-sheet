"""Переменные и типы. = это «положи справа в имя слева», не «равно»."""

name = "Аня"          # str   текст
age = 25              # int   целое (размер не ограничен)
height = 1.72         # float дробное, приближённо (0.1+0.2 != 0.3)
is_ok = True          # bool  только True / False  (с большой буквы)
nothing = None        # «значения нет»

print(type(age))      # <class 'int'>
print(type(name), type(height), type(is_ok), type(nothing))

x = 5
x = x + 1             # взяли 5, прибавили 1, положили 6
x += 1                # то же короче
x = "теперь строка"   # динамика: имя может сменить тип

# имена: латиница, цифры не сначала, _; стиль snake_case
user_name = "Аня"
# 2name = "нет"       # SyntaxError
# user-name = "нет"   # минус — это вычитание
# if = 1              # нельзя: if, for, class, def, return...

a, b = 1, 2           # множественное присваивание
a, b = b, a           # обмен без третьей переменной
print("обмен:", a, b) # 2 1

PI = 3.14             # ЗАГЛАВНЫЕ = константа по договорённости (менять можно)

# --- преобразование ---
print(int("42"))      # 42
print(int(7.9))       # 7   дробь ОТБРАСЫВАЕТСЯ, не округляется
print(float("3.14"))  # 3.14
print(float(5))       # 5.0
print(str(99))        # "99"
print(bool(0), bool(""), bool([]), bool(None))  # False False False False
print(bool("0"), bool("нет"), bool([0]))        # True True True  непустое = истина
print(int(True), int(False))                    # 1 0

# "возраст: " + 25     # TypeError — строка + число нельзя
print("возраст: " + str(25))
print(f"возраст: {25}")                         # лучше f-строка

# int("3.5")           # ValueError — сначала float, потом int
# int("abc")           # ValueError
# int(input()) если введут «двадцать» → ValueError
