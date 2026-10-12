"""ООП: класс — чертёж, объект — экземпляр. self — «этот объект» (то, что слева от точки)."""


class Counter:
    def __init__(self, start=0):       # конструктор, вызывается при Counter(10)
        self.value = start             # атрибут ЭКЗЕМПЛЯРА — свой у каждого

    def inc(self, step=1):             # метод = функция внутри класса
        self.value += step
        return self.value

    def __str__(self):                 # print(obj) — для людей
        return f"счётчик({self.value})"

    def __repr__(self):                # в консоли и списках — для разработчика
        return f"Counter({self.value!r})"


c = Counter(10)
print(c.inc())                         # 11
print(Counter.inc(c, 5))               # 16 — то же явно: self = c
print(c)


class User:
    count = 0                          # атрибут КЛАССА — общий

    def __init__(self, name):
        self.name = name
        self.tags = []                 # изменяемое — только в __init__, НЕ tags = [] в теле класса
        User.count += 1


# property: метод выглядит как атрибут, с проверкой при записи
class Product:
    def __init__(self, price):
        self.price = price             # пройдёт через setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("цена ≥ 0")
        self._price = value


p = Product(100)
print(p.price)
# p.price = -1                         # ValueError


class Temperature:
    def __init__(self, c):
        self.c = c

    @classmethod
    def from_f(cls, f):                # фабрика: cls — сам класс
        return cls((f - 32) * 5 / 9)

    @staticmethod
    def freezing(c):                   # без self и cls — просто функция рядом
        return c <= 0


print(Temperature.from_f(212).c)       # 100


# наследование: Manager IS-A Employee. super() — родитель
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary

    def pay(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def pay(self):                     # переопределили
        return self.salary + self.bonus

staff = [Employee("Аня", 80), Manager("Борис", 100, 30)]
for person in staff:
    print(person.name, person.pay())   # полиморфизм: один вызов — разные реализации

# композиция: «у машины ЕСТЬ двигатель», а не «машина ЯВЛЯЕТСЯ двигателем»

from dataclasses import dataclass, field

@dataclass
class Task:
    title: str
    done: bool = False
    tags: list = field(default_factory=list)  # НЕ tags: list = []

    def complete(self):
        self.done = True

print(Task("хлеб"))                    # Task(title='хлеб', done=False, tags=[])
# frozen=True — неизменяемый, можно в set
# __eq__ переопределили — определи и __hash__, иначе не ключ словаря
