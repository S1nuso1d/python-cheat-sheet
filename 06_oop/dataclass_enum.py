"""dataclass — класс-хранилище без ручного __init__/__repr__. Enum — именованные константы."""

from dataclasses import dataclass, field, asdict
from datetime import date
from enum import Enum, auto


class Priority(Enum):
    LOW = 1
    MID = 2
    HIGH = 3


@dataclass
class Task:
    title: str
    priority: Priority = Priority.MID
    due: date | None = None
    done: bool = False
    tags: list[str] = field(default_factory=list)  # НЕ tags: list = []

    def complete(self) -> None:
        self.done = True

    @property
    def is_overdue(self) -> bool:
        return bool(self.due and not self.done and self.due < date.today())


t = Task("хлеб", tags=["дом"])
t.complete()
print(t)
print(asdict(t))                       # → обычный dict (для JSON)
print(Priority.HIGH.name, Priority.HIGH.value)

# @dataclass(frozen=True) — нельзя менять поля, можно класть в set / ключ dict
# __post_init__ — валидация сразу после создания
# StrEnum (3.11+) — значения-строки, удобно в JSON/БД
