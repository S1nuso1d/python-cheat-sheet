"""lambda, sorted/key, замыкание, nonlocal. Короткое имя функции лучше длинной лямбды."""

# lambda args: выражение   — однострочная функция, return не пишут
square = lambda x: x * x
print(square(5))

# главное место — key= у sorted / min / max / .sort
users = [{"name": "Борис", "age": 30}, {"name": "Аня", "age": 25}]
print(sorted(users, key=lambda u: u["age"]))
print(sorted(["b", "Aaa", "c"], key=str.lower))
print(max(users, key=lambda u: u["age"])["name"])   # Борис

# map/filter есть, но включения обычно читаемее
print(list(map(str.upper, ["a", "b"])))
print(list(filter(lambda x: x > 0, [-1, 2, 0])))
print([x for x in [-1, 2, 0] if x > 0])             # то же яснее

from functools import partial
def power(base, exp):
    return base ** exp

square2 = partial(power, exp=2)
print(square2(5))                      # 25


# --- замыкание: внутренняя функция помнит переменные внешней ---
def make_adder(n):
    def add(x):
        return x + n                   # n «захвачен»
    return add

plus10 = make_adder(10)
print(plus10(5))                       # 15


# nonlocal — переприсвоить имя из ВНЕШНЕЙ (не global) функции
def counter():
    n = 0
    def tick():
        nonlocal n
        n += 1
        return n
    return tick

t = counter()
print(t(), t())                        # 1 2

# ловушка цикла + лямбда:
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])            # [2, 2, 2]  все смотрят на финальную i
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])            # [0, 1, 2]  значение зафиксировали
