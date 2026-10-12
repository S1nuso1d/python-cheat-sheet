"""async/await: пока ждём сеть/БД — делаем другие запросы. Не для тяжёлой арифметики."""

import asyncio

# async def — корутина: вызов НЕ выполняет код, нужен await или gather
# event loop переключается в точках await


async def slow(name: str, sec: float) -> str:
    await asyncio.sleep(sec)               # НЕ time.sleep — тот стопорит ВСЕХ
    return name


async def main():
    # параллельно, общее время ≈ max, не сумма
    a, b = await asyncio.gather(slow("A", 0.1), slow("B", 0.1))
    print(a, b)

asyncio.run(main())

# httpx.AsyncClient вместо requests
# SQLAlchemy: create_async_engine + AsyncSession + asyncpg
# Semaphore(5) — не больше 5 запросов сразу
# asyncio.to_thread(blocking_fn) — вынести синхронный код

# GIL: в один момент байт-код одного потока.
#   ждать сеть     → async или threading
#   считать ядра   → multiprocessing
# в FastAPI: async def + внутри requests.get = стоп сервера

print("gather = параллельно ждать; sleep/requests в async def — враги")
