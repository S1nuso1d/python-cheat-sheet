"""Включения, генераторы, декораторы — короткий «питонический» код."""

nums = [3, -1, 4, -5, 9]
print([n ** 2 for n in nums if n > 0])          # список  [9, 16, 81]
print({n % 3 for n in nums})                    # множество
print({n: n ** 2 for n in nums if n > 0})       # словарь
print(sum(x * x for x in range(1_000_000)))     # генераторное выражение — мало памяти
# если включение не читается с первого раза — пиши обычный цикл

# генератор: yield отдаёт значение и ЗАПОМИНАЕТ место. Одноразовый, len() нельзя
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(list(countdown(3)))                       # [3, 2, 1]

def chunks(items, size):
    buf = []
    for x in items:
        buf.append(x)
        if len(buf) == size:
            yield buf
            buf = []
    if buf:
        yield buf

print(list(chunks(range(5), 2)))                # [[0,1],[2,3],[4]]

# файлы/логи: for line in f — уже генератор, не грузи 5 ГБ через readlines()

# декоратор: @timer  ==  f = timer(f)  обернуть поведение вокруг функции
from functools import wraps, lru_cache
import time

def timer(func):
    @wraps(func)                                # сохранить имя и докстринг
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)          # обязательно вернуть результат
        print(func.__name__, f"{time.perf_counter() - t0:.4f}с")
        return result
    return wrapper

@lru_cache                                      # кэш чистой функции
def fib(n):
    return n if n < 2 else fib(n - 1) + fib(n - 2)

print("fib(30) =", fib(30))                     # без кэша — вечность

# декоратор с параметрами — три уровня: def retry(times): def deco(func): def wrapper...
# несколько @: снизу вверх
