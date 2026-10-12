"""Множество (set) — уникальные элементы, проверка in мгновенная. Порядка нет."""

tags = {"python", "backend", "python"}
print(tags)                        # дубль исчез
tags.add("sql")
tags.discard("backend")            # нет элемента — молча
# tags.remove("нет")               # KeyError, если нет
print("sql" in tags)
# tags[0]                          # TypeError: индексов нет

print(set())                       # пустое.  {}  это СЛОВАРЬ, не множество
print(set("abba"))                 # {'a', 'b'}
print(set([1, 2, 2, 3]))           # {1, 2, 3}

a, b = {1, 2, 3, 4}, {3, 4, 5}
print(a | b)                       # объединение {1,2,3,4,5}
print(a & b)                       # пересечение {3, 4}
print(a - b)                       # есть в a, нет в b  {1, 2}
print(a ^ b)                       # симметричная разность {1, 2, 5}
print({1, 2} <= a)                 # подмножество?
print(a.isdisjoint({9}))           # нет общих?

# те же операции методами: union, intersection, difference, ...

# типовые задачи:
# дубли (порядок потеряется):  list(set(items))
# общие курсы:                 set(a) & set(b)
# новые относительно вчера:    set(today) - set(yesterday)

# порядок важен? не set, а цикл:
def unique(items):
    out = []
    for x in items:
        if x not in out:
            out.append(x)
    return out

# элемент только хешируемый (не list). frozenset — неизменяемое, можно ключом dict.

# скорость:  999999 in list_of_million  — медленно
#            999999 in set_of_million   — мгновенно
