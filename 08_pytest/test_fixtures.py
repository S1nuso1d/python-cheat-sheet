"""Рабочие тесты фикстур и моков. pytest 08_pytest/test_fixtures.py -v"""

import os

import pytest


@pytest.fixture
def cart():
    return ["хлеб", "молоко"]


def test_cart_isolated(cart):
    cart.append("сыр")
    assert "сыр" in cart


def test_cart_fresh(cart):
    assert cart == ["хлеб", "молоко"]          # предыдущий тест не оставил сыр


def test_write_file(tmp_path):
    p = tmp_path / "a.txt"
    p.write_text("привет", encoding="utf-8")
    assert p.read_text(encoding="utf-8") == "привет"


def test_print_capsys(capsys):
    print("ok")
    assert "ok" in capsys.readouterr().out


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


def test_env(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "secret")
    assert os.getenv("API_TOKEN") == "secret"


def clock() -> str:
    return "живые-часы"


def greet() -> str:
    return f"сейчас {clock()}"


def test_monkeypatch_func(monkeypatch):
    import sys
    monkeypatch.setattr(sys.modules[__name__], "clock", lambda: "2026-01-01")
    assert greet() == "сейчас 2026-01-01"


def test_conftest_user(sample_user):
    assert sample_user["email"].endswith("@test.ru")


@pytest.mark.skip(reason="пример пропуска")
def test_skip_demo():
    assert False


@pytest.mark.xfail(reason="известный пример")
def test_xfail_demo():
    assert 1 == 0
