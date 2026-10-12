"""Циклы: while (пока неизвестно сколько), for (для каждого), range."""

# --- while: 3 части — старт, условие, шаг. Без шага = бесконечный цикл (Ctrl+C)
count = 3
while count > 0:
    print("осталось", count)
    count -= 1                     # шаг

# аккумулятор
total, n = 0, 1
while n <= 5:
    total += n
    n += 1
print("сумма 1..5:", total)        # 15

# бесконечный + break  — валидация ввода (выучи наизусть)
# while True:
#     line = input("1..10: ").strip()
#     if line.isdigit():
#         value = int(line)
#         if 1 <= value <= 10:
#             break
#     print("ещё раз")

# continue — пропустить остаток ЭТОГО круга
n = 0
while n < 5:
    n += 1                         # шаг ДО continue, иначе зависнешь
    if n == 3:
        continue
    print(n, end=" ")              # 1 2 4 5
print()

# while/for else: сработает, если НЕ было break
for x in []:
    print("не зайдём")
else:
    print("else у цикла")

# --- for: для каждого элемента (шаг забыть нельзя)
for letter in "Py":
    print(letter)

# range(start, stop, step)  stop НЕ входит
print(list(range(5)))              # 0 1 2 3 4
print(list(range(2, 6)))           # 2 3 4 5
print(list(range(1, 10, 3)))       # 1 4 7
print(list(range(10, 0, -3)))      # 10 7 4 1
print(list(range(5, 5)))           # []  пустой
# 1..10 включительно: range(1, 11)   ошибка «на единицу»

# enumerate — номер + элемент; zip — два списка рядом
words = ["хлеб", "молоко"]
for i, w in enumerate(words, start=1):
    print(f"{i}. {w}")
for w, p in zip(words, [50, 80]):
    print(w, p)

print(sum(range(1, 5)))            # 1+2+3+4=10
print(any(x < 0 for x in [1, -2]), all(x > 0 for x in [1, 2]))

# когда что: «для каждого / от A до B» → for; «пока не стоп / не угадали» → while

# --- вложенный: внешний шаг → внутренний крутится ЦЕЛИКОМ
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end="")
    print()                        # перевод строки после внутренней

# пары без повторов (i, j) и (j, i):
xs = [1, 3, 5]
for i in range(len(xs)):
    for j in range(i + 1, len(xs)):
        print(xs[i], xs[j])        # 1 3 / 1 5 / 3 5

# break во внутреннем выходит только из внутреннего
# N×N циклов при N=100_000 — уже слишком много операций
