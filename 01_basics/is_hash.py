"""== vs is, id, hash. Сравнивать значения — ==. Сравнивать «тот же объект» — is."""

a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)          # True False True
print(id(a), id(c))                    # одинаковый адрес у a и c

# is только для None / True / False (синглтоны)
x = None
print(x is None, x is not None)
# if x == None:  работает, но стиль — is

# мелкие int (-5..256) Python кэширует — is может случайно совпасть. Для значений всегда ==

# hash нужен ключу dict / элементу set: неизменяемый объект
print(hash("аня"), hash((1, 2)))
# hash([1, 2])                         # TypeError — список меняется
# ключ dict: str, int, tuple из неизменяемого. list/dict/set — нет

# свой класс в set: определи И __eq__, И __hash__ согласованно
# если __eq__ по полям — hash тоже из тех же полей; frozen dataclass делает сам
