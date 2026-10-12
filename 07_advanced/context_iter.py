"""Итераторы и контекстные менеджеры. for x in obj ходит через iter → next до StopIteration."""

nums = [10, 20]
it = iter(nums)                        # список → итератор (одноразовый курсор)
print(next(it), next(it))
# next(it)                             # StopIteration

# свой итератор: __iter__ верни self, __next__ отдай или брось StopIteration
# генератор (yield) — уже итератор, проще чем класс

# файл из open() — контекстный менеджер: есть __enter__/__exit__


class FakeLock:
    def __enter__(self):
        print("взяли")
        return self                    # то, что попадёт в as

    def __exit__(self, exc_type, exc, tb):
        print("отдали")                # вызовется даже при ошибке
        return False                   # False = не глотать исключение

with FakeLock() as lock:
    print("внутри", lock)

from contextlib import contextmanager, suppress, closing

@contextmanager
def timer_cm():
    print("start")
    yield "ok"
    print("end")

with timer_cm() as msg:
    print(msg)

with suppress(FileNotFoundError):      # проглотить конкретную ошибку
    open("нет_такого.txt", encoding="utf-8")

# with a, b:  несколько ресурсов
# свой класс с close() → closing(obj) из contextlib
print("итератор одноразовый; with гарантирует закрытие")
