"""Общие фикстуры папки. pytest подхватит сам, импортировать не надо."""

import pytest


@pytest.fixture
def sample_user() -> dict:
    return {"id": 1, "email": "anya@test.ru", "active": True}
