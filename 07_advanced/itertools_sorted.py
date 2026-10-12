"""itertools, any/all, sorted. Комбинации и группировки без своих вложенных циклов."""

from itertools import count, islice, chain, groupby, product, combinations

print(list(islice(count(10, 2), 4)))   # 10 12 14 16  бесконечный счётчик обрезали
print(list(chain([1, 2], [3], "ab")))  # склеить итерируемые

rows = [("a", 1), ("a", 2), ("b", 9)]
for key, group in groupby(rows, key=lambda r: r[0]):
    print(key, list(group))            # groupby требует УЖЕ отсортированное по ключу

print(list(product("AB", "12")))       # все пары  A1 A2 B1 B2
print(list(combinations([1, 2, 3], 2)))  # (1,2)(1,3)(2,3)  без повторов порядка

print(any(x > 10 for x in [1, 20]))    # True — есть хотя бы один
print(all(x > 0 for x in [1, 2]))      # True — все
print(next(x for x in [0, 3, 5] if x > 0), "нет")  # первый подходящий

items = ["bbb", "a", "cc"]
print(sorted(items, key=len))          # по длине
print(sorted(items, key=lambda s: (-len(s), s)))  # длинные первые, при равенстве алфавит

# reversed(seq) — с конца; enumerate(seq, start=1) — номер
# zip(a, b, strict=True)  3.10+ ошибка, если длины разные
# zip_longest из itertools — дырки заполняет fillvalue
