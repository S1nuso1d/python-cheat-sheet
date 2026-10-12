"""Маркеры, моки, conftest, покрытие. Справочник — рабочие тесты в test_*.py."""

# @pytest.mark.skip(reason="пока чиним")
# @pytest.mark.skipif(sys.platform == "win32", reason="только linux")
# @pytest.mark.xfail(reason="известный баг")   ждём падение; если вдруг прошёл — pytest сообщит
# @pytest.mark.slow                         свой маркер; запуск: pytest -m "not slow"

# pytest.ini:
#   [pytest]
#   testpaths = tests
#   markers =
#       slow: долгие тесты
#   filterwarnings = error

# conftest.py кладут в tests/ — фикстуры видны всем тестам папки БЕЗ импорта
# вложенный conftest перекрывает верхний для своей папки

# monkeypatch.setattr(module, "func", fake)
# monkeypatch.setenv("KEY", "value")
# monkeypatch.chdir(tmp_path)
# monkeypatch.syspath_prepend(str(tmp_path))

# unittest.mock.MagicMock: возвращает моки на любой атрибут
# mock.assert_called_once_with(1, 2)
# mock.call_count
# patch("пакет.модуль.имя")  патчить ТАМ, ГДЕ ИСПОЛЬЗУЮТ, не где определили

# покрытие:
#   pip install pytest-cov
#   pytest --cov=app --cov-report=term-missing
# 100% не цель; важны ветки с if/except и границы

# структура:
#   tests/conftest.py
#   tests/test_users.py
#   tests/api/test_tasks.py
# имя файла test_*.py, функции test_*, классы Test*
# тестам не нужен __init__.py (в pytest 7+ лучше без него — меньше сюрпризов импорта)
