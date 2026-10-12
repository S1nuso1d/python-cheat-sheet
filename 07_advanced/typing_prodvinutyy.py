"""Typing глубже: Literal, TypedDict, TypeVar, Generic, Self, Final, NewType."""

from typing import Final, Literal, TypedDict, TypeVar, Generic, NewType, Self


Mode = Literal["low", "mid", "high"]   # только эти три строки

def set_mode(mode: Mode) -> None:
    print("mode", mode)

set_mode("mid")
# set_mode("ultra")                    # mypy/IDE ругнется, Python на рантайме пропустит


class UserDict(TypedDict):
    id: int
    email: str
    active: bool                       # все ключи обязательны

u: UserDict = {"id": 1, "email": "a@b.ru", "active": True}


T = TypeVar("T")                       # «тот же тип вошёл и вышел»


def first(items: list[T]) -> T | None:
    return items[0] if items else None

print(first([1, 2]), first(["a"]))     # типы: int | None  и  str | None


class Box(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value

print(Box(42).get())


class Player:
    def spawn(self) -> Self:           # вернуть экземпляр СВОЕГО класса (и наследника)
        return self


MAX_LIMIT: Final[int] = 100            # договорённость «не менять» + проверка mypy
UserId = NewType("UserId", int)        # int, но не смешивай с «просто числом»
uid = UserId(7)

# Optional[X] = X | None
# Sequence[X] — list/tuple по индексу; Mapping[K,V] — dict-подобное только чтение
# Callable[[int, str], bool] — функция двух аргументов
# from collections.abc import Iterable, Sequence  (предпочтительнее typing.List)
# FastAPI смотрит аннотации ВРАНТАЙМЕ; mypy — статически. Это разные проверки
