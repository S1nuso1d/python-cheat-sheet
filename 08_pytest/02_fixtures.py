"""Фикстуры и параметризация — подготовка данных и много случаев одним тестом."""

import pytest


# фикстура: pytest САМ вызовет и подставит аргумент с тем же именем
@pytest.fixture
def cart():
    return ["хлеб", "молоко"]          # каждый тест получит СВОЙ список


def test_cart_len(cart):
    assert len(cart) == 2


def test_cart_append(cart):
    cart.append("сыр")
    assert "сыр" in cart               # не влияет на другой тест


# tmp_path — временная папка, после теста удалится
def test_write_file(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("привет", encoding="utf-8")
    assert p.read_text(encoding="utf-8") == "привет"


# capsys — поймать print
def test_print(capsys):
    print("ok")
    captured = capsys.readouterr()
    assert "ok" in captured.out


# параметризация: 1 функция → N прогонов
@pytest.mark.parametrize("value,expected", [
    ("", False),
    ("abc", False),
    ("Qwerty1!", True),
    ("12345678", False),
])
def test_password(value, expected):
    def strong(p: str) -> bool:
        return len(p) >= 8 and any(c.isdigit() for c in p) and any(c.isupper() for c in p)
    assert strong(value) is expected


# monkeypatch — подменить окружение / функцию на время теста
def test_env(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "secret")
    import os
    assert os.getenv("API_TOKEN") == "secret"


# scope="module" — фикстура один раз на файл (БД, тяжёлое)
# conftest.py в папке tests — общие фикстуры без импорта
# pytest --cov=app          покрытие
# тест на баг: сначала падающий тест, потом фикс — так и коммить
