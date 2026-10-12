"""Исключения: ошибка — объект. Не поймали — программа упала. Лови КОНКРЕТНЫЙ тип."""

# try: опасное
# except Тип: что делать
# else: если ошибки не было
# finally: всегда (закрыть файл и т.п.)

line = "25"
try:
    age = int(line)
    print(100 / age)
except ValueError:
    print("нужно целое число")
except ZeroDivisionError:
    print("на ноль нельзя")
except (TypeError, OverflowError) as e:
    print("другое:", e)
else:
    print("ок")
finally:
    print("этот блок всегда")

# except ValueError as e:  e — сообщение
# except:  и except Exception:  прячут баги — не надо
# except: pass  — ещё хуже

# бросить самому
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("сумма > 0")
    if amount > balance:
        raise ValueError("не хватает денег")
    return balance - amount

try:
    withdraw(100, 500)
except ValueError as e:
    print("отказ:", e)


class InsufficientFunds(Exception):
    """Своё исключение — по имени понятно, что случилось."""


# карта частых
# SyntaxError        опечатка синтаксиса, нет : или кавычки
# IndentationError   сбит отступ
# NameError          имени нет / опечатка
# TypeError          "5"+5, None*2
# ValueError         int("abc") — тип тот, значение плохое
# IndexError/KeyError нет индекса / ключа
# ZeroDivisionError  / 0
# FileNotFoundError  нет файла
# AttributeError     нет метода/атрибута

# трейсбэк читай СНИЗУ ВВЕРХ: последняя строка — тип и смысл, выше — файл и номер
# assert условие, "текст"  — для инвариантов в разработке, не для ввода пользователя

# цепочка: не теряй исходную причину
try:
    int("x")
except ValueError as e:
    try:
        raise RuntimeError("не смогли прочитать id") from e
    except RuntimeError as wrapped:
        print("причина:", wrapped.__cause__)     # исходный ValueError
# raise ... from None  — наоборот, спрятать причину (редко нужно)
# finally закрывает ресурс; контекстный менеджер (with) обычно лучше ручного finally
