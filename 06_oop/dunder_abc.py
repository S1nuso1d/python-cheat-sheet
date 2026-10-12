"""Дандер-методы и контракты (ABC / Protocol). obj + 1 вызывает obj.__add__(1)."""

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Money:
    def __init__(self, amount: int):
        self.amount = amount

    def __repr__(self) -> str:
        return f"Money({self.amount})"

    def __str__(self) -> str:          # print / f-строка
        return f"{self.amount} ₽"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Money) and self.amount == other.amount

    def __hash__(self) -> int:         # раз есть __eq__ — нужен и hash (неизменяемый смысл)
        return hash(self.amount)

    def __lt__(self, other: "Money") -> bool:
        return self.amount < other.amount

    def __add__(self, other: "Money") -> "Money":
        return Money(self.amount + other.amount)

    def __len__(self) -> int:
        return self.amount             # редкость, для примера

print(Money(10) + Money(5), Money(10) == Money(10))
print(sorted([Money(30), Money(10)]))  # нужен __lt__


# контейнер: __getitem__  obj[i]     __iter__  for x in obj
class Pair:
    def __init__(self, a, b):
        self._data = (a, b)

    def __getitem__(self, i):
        return self._data[i]

    def __iter__(self):
        return iter(self._data)

print(Pair("a", "b")[1], list(Pair(1, 2)))


# ABC — «наследник обязан реализовать»
class Repository(ABC):
    @abstractmethod
    def get(self, id: int) -> dict | None: ...


class MemoryRepo(Repository):
    def get(self, id: int) -> dict | None:
        return {"id": id}


# Protocol — утиная типизация: не надо наследовать, достаточно методов
@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class Handle:
    def close(self) -> None:
        pass

print(isinstance(Handle(), Closable))  # True благодаря runtime_checkable
# Repository()                         # TypeError: нельзя создать абстрактный
print(MemoryRepo().get(1))
