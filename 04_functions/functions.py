"""Функции: кусок кода с именем. Считает — return. Печатает — print. Не смешивать."""

def greet(name, greeting="Привет"):
    """Короткое описание в первой строке. Видно в help(greet)."""
    return f"{greeting}, {name}!"      # return ОТДАЁТ значение и сразу выходит

print(greet("Аня"))                    # Привет, Аня!
print(greet("Аня", greeting="Салют"))  # именованный аргумент, порядок не важен

def add_bad(a, b):
    print(a + b)                       # показал и потерял → вернёт None

def add_good(a, b):
    return a + b

y = add_good(2, 3)
print(y * 2)                           # 10
# add_bad(2, 3) * 2                    # TypeError: None * int

# несколько значений = кортеж
def stats(xs):
    if not xs:
        return None, None, None
    return min(xs), max(xs), sum(xs) / len(xs)

lo, hi, avg = stats([4, 8, 6])

# ранний return спрямляет if
def letter(avg):
    if avg is None:
        return "нет данных"
    if avg >= 90:
        return "отлично"
    if avg >= 75:
        return "хорошо"
    return "слабо"


# --- аргументы ---
def order(item, qty=1, *, discount=0):
    """После * — только по имени: order("хлеб", discount=10)."""
    return item, qty, discount

print(order("хлеб"), order("хлеб", 3), order(item="хлеб", qty=2))

def total(*prices, currency="руб"):     # *args = кортеж лишних позиционных
    return f"{sum(prices)} {currency}"

print(total(10, 20, 30), total(*[10, 20], currency="₽"))

def build_url(base, **params):          # **kwargs = словарь именованных
    q = "&".join(f"{k}={v}" for k, v in params.items())
    return f"{base}?{q}" if params else base

print(build_url("https://api", page=2, limit=10))


# --- ЛОВУШКА: изменяемое значение по умолчанию ---
def add_bad_default(item, box=[]):      # список создаётся ОДИН раз
    box.append(item)
    return box

print(add_bad_default(1))               # [1]
print(add_bad_default(2))               # [1, 2]  сюрприз

def add_ok(item, box=None):
    if box is None:
        box = []
    box.append(item)
    return box


# --- область видимости ---
# имя внутри функции снаружи не видно
# присваивание внутри создаёт ЛОКАЛЬНУЮ; global почти не нужен
def bump(n):
    return n + 1                        # передали — вернули

# мутация аргумента меняет объект у вызывающего
def add_mut(cart, item):
    cart.append(item)                   # портит чужой список

def add_pure(cart, item):
    return cart + [item]                # старый цел


# словарь операций вместо длинного if
def add(a, b): return a + b
def sub(a, b): return a - b
ops = {"+": add, "-": sub}
print(ops["+"](2, 3))


# рекурсия: базовый случай + шаг к нему
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))
# RecursionError если нет базового случая / слишком глубоко (~1000)
# fib рекурсией без кэша — медленно: одни и те же значения считаются снова
