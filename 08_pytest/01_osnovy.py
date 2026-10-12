"""
pytest — тесты как обычные функции test_*.
Запуск из папки cheat_sheet_python:
    pytest 08_pytest -v
    pytest 08_pytest -k add          только тесты с «add» в имени
    pytest 08_pytest --lf            только упавшие в прошлый раз
"""

# Файл должен называться test_*.py  (этот — справочник, его pytest может подхватить
# из-за test_ внутри. Реальные тесты: test_primery.py рядом.)

# assert условие           если ложь — pytest покажет оба значения
# одна мысль на тест
# тесты независимы: не должны требовать порядок запуска


def add(a: int, b: int) -> int:
    return a + b


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("на ноль нельзя")
    return a / b


def test_divide_ok():
    assert divide(10, 4) == 2.5


def test_divide_zero():
    import pytest
    with pytest.raises(ZeroDivisionError, match="ноль"):
        divide(1, 0)


def test_float_approx():
    import pytest
    assert 0.1 + 0.2 == pytest.approx(0.3)   # не == 0.3


# что проверять: нормальный случай + границы (0, пустой список, None) + ошибка
# не ходи в интернет и не пиши в боевые файлы — tmp_path / моки
