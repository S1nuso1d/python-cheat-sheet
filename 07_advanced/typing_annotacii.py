"""Аннотации типов: подсказки для тебя, IDE и mypy. Python их во время работы НЕ проверяет."""

from typing import Any, Callable, Iterable

def total(prices: list[float], discount: float = 0.0) -> float:
    return sum(prices) * (1 - discount)

def find_user(user_id: int) -> dict[str, Any] | None:   # может вернуть None
    return None

Handler = Callable[[str], bool]          # псевдоним: функция str → bool

def apply(fn: Handler, text: str) -> bool:
    return fn(text)

print(total([10.0, 20.0], 0.1))          # 27.0

# современный стиль 3.10+:  list[str]  dict[str, int]  int | None
# старый:                   List[str]  Dict[str, int]  Optional[int]

# в классах и dataclass аннотации обязательны для генерации полей
# mypy app     — проверка; FastAPI/Pydantic БЕРУТ типы всерьёз (валидация входа)
