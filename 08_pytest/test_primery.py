"""Рабочие тесты. Запуск: pytest 08_pytest/test_primery.py -v"""

import pytest


def unique(items: list) -> list:
    out = []
    for x in items:
        if x not in out:
            out.append(x)
    return out


def test_unique_keeps_order():
    assert unique([3, 1, 3, 2, 1]) == [3, 1, 2]


def test_unique_empty():
    assert unique([]) == []


@pytest.mark.parametrize("n,want", [(2, True), (9, False), (1, False), (97, True)])
def test_is_prime(n, want):
    def is_prime(x: int) -> bool:
        if x < 2:
            return False
        d = 2
        while d * d <= x:
            if x % d == 0:
                return False
            d += 1
        return True
    assert is_prime(n) is want


def test_tmp_json(tmp_path):
    import json
    p = tmp_path / "t.json"
    p.write_text(json.dumps({"ok": True}, ensure_ascii=False), encoding="utf-8")
    assert json.loads(p.read_text(encoding="utf-8"))["ok"] is True
