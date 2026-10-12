"""SQL: база = таблицы. Пишешь ЧТО хочешь, база решает КАК. Параметры только через ?."""

# SELECT поля FROM таблица
# WHERE фильтр          до группировки
# GROUP BY поле
# HAVING фильтр групп    после группировки
# ORDER BY поле DESC
# LIMIT n OFFSET m

# JOIN  — склеить таблицы по ключу
# INNER JOIN  только пары
# LEFT  JOIN  все слева, нет пары → NULL
# «клиенты без заказов»:
#   FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
#   WHERE o.id IS NULL

# агрегаты: COUNT(*)  SUM  AVG  MIN  MAX
# всё не-агрегат в SELECT должно быть в GROUP BY
# COUNT(column) не считает NULL; COUNT(*) считает строки

# NULL — «неизвестно»:  = NULL не работает, только IS NULL
# CASE WHEN price > 1000 THEN 'дорого' ELSE 'ок' END

# Python sqlite3 — НИКОГДА f-строка в SQL (инъекция):
#   cur.execute("SELECT * FROM u WHERE name = ?", (name,))   # хорошо
#   cur.execute(f"SELECT * FROM u WHERE name = '{name}'")    # катастрофа

# транзакция: перевод денег = списать И зачислить, иначе rollback
# индекс ускоряет WHERE/JOIN по полю, замедляет INSERT
# ORM (SQLAlchemy): классы ↔ таблицы; N+1 = в цикле лениво грузят детей
#   лечится selectinload / JOIN
# Alembic — миграции схемы (добавил поле → revision → upgrade)

print("шпаргалка SQL, запросы руками в sql-ex.ru / sqliteonline.com")
print("WHERE vs HAVING | INNER vs LEFT | ? вместо f-строки | JOIN трёх таблиц")
