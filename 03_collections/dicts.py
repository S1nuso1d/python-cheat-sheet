"""Словарь (dict) — ключ → значение. Поиск по ключу почти мгновенный."""

user = {"name": "Аня", "age": 25, "city": "Пермь"}
print(user["name"])                # Аня
# user["phone"]                    # KeyError, если ключа нет
print(user.get("phone"))           # None  без ошибки
print(user.get("phone", "нет"))    # значение по умолчанию

user["age"] = 26                   # изменить
user["email"] = "a@mail.ru"        # добавить
del user["city"]                   # удалить
print("age" in user)               # True  in проверяет КЛЮЧИ, не значения
print("Аня" in user)               # False
print("Аня" in user.values())

print(user.pop("age", None))       # снять ключ; нет — вернуть None
user.setdefault("city", "Пермь")   # записать, только если ключа ещё нет

# создание
print({})                          # пустой словарь (НЕ множество)
print(dict(name="Аня", age=25))
print(dict(zip(["a", "b"], [1, 2])))
print(dict.fromkeys(["a", "b"], 0))

# обход
user = {"name": "Аня", "age": 25}
for key in user:                   # по ключам
    print(key, user[key])
for key, value in user.items():    # так чаще всего
    print(f"{key}: {value}")
print(list(user.keys()), list(user.values()))

# ключ — только неизменяемый: str, int, tuple. Не list, не dict.
# значение — что угодно, включая список и другой словарь.
# с 3.7 порядок ключей = порядок добавления

# счётчик слов
counter = {}
for word in "и раз и два и три".split():
    counter[word] = counter.get(word, 0) + 1
print(counter)                     # {'и': 3, 'раз': 1, ...}

# топ по значению
top = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
print(top[:2])

# вложенность
data = {"user": {"address": {"city": "Пермь"}}}
print(data["user"]["address"]["city"])
print(data.get("user", {}).get("phone"))  # None, не KeyError

# объединение: правый побеждает
a, b = {"x": 1, "y": 2}, {"y": 9, "z": 3}
print({**a, **b})                  # {'x': 1, 'y': 9, 'z': 3}
print(a | b)                       # то же, 3.9+

# инверсия: цена → список товаров
catalog = {"хлеб": 50, "чай": 50, "мёд": 300}
by_price = {}
for name, price in catalog.items():
    by_price.setdefault(price, []).append(name)
print(by_price)                    # {50: ['хлеб', 'чай'], 300: ['мёд']}

# список словарей — типичные «живые» данные
users = [
    {"name": "Аня", "age": 25},
    {"name": "Борис", "age": 31},
]
print(sorted(users, key=lambda u: u["age"], reverse=True))
print([u for u in users if u["age"] >= 30])
print(sum(u["age"] for u in users) / len(users))
