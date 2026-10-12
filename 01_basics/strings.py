"""Строки (str) — НЕИЗМЕНЯЕМЫЕ. Метод возвращает НОВУЮ строку."""

s = "Python"
# индекс  0 1 2 3 4 5
#         P y t h o n
# с конца-6-5-4-3-2-1
print(s[0], s[-1], len(s))     # P n 6
# s[0] = "p"                   # TypeError — нельзя менять символ
# s[6]                         # IndexError

# срез [start:stop:step]  stop НЕ входит; срез за границей НЕ падает
print(s[1:4])                  # yth
print(s[:2], s[2:], s[-2:])    # Py  thon  on
print(s[::2], s[::-1])         # Pto  nohtyP
print(s[100:])                 # ''

raw = "  Иван Петров  "
name = raw.strip()             # срезать пробелы по краям
print(name.lower())            # иван петров
print(name.upper())            # ИВАН ПЕТРОВ
print(name.title())            # Иван Петров
print(name.capitalize())       # Иван петров  (только первая буква СТРОКИ)
print(name.split())            # ['Иван', 'Петров']  по пробелам, пустые выкидывает
print("а, б,  в".split(","))   # ['а', ' б', '  в']  пробелы вокруг остаются
print("-".join(["2026", "09", "12"]))   # 2026-09-12  join у РАЗДЕЛИТЕЛЯ
print(name.replace("Иван", "Пётр"))
print("Иван" in name)          # True  подстрока
print(name.startswith("Ив"), name.endswith("ров"))
print("abab".count("ab"))      # 2
print(name.find("Петр"))       # 5  или -1 если нет
# name.index("XXX")            # ValueError, если нет
print("42".isdigit(), "42a".isdigit())  # True False
print("abc".isalpha(), " ".isspace())

print("ха" * 3)                # хахаха
print("a" + "b")               # ab  для текста с переменными бери f-строку
print("Иван" == "иван")        # False — перед сравнением .lower()

# цепочка методов: каждый возвращает новую строку
print("  A B  ".strip().lower().replace(" ", "_"))  # a_b

# экранирование
print("C:\\Users\\me")         # путь со слэшами
print(r"C:\Users\me")          # r-строка: слэши как есть

# многострочный: """..."""
# склейка в цикле через + — плохо (новая строка каждый раз)
# собирай список и делай "".join(parts)
