"""
Задание 3
Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем.
В случае базового класса это может быть строка Создайте от него три производных класса: President, Manager, Worker.
Переопределите функцию Print() длявывода информации, соответствующей каждому типу служащего.


Задание 4
Для классов из задания 3 реализуйте магический метод str, а также метод int (должен возвращать возраст служащего).
"""


class Employer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        pass

class Manager(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f"Менеджер {self.name}, возраст {self.age}")

class Worker(Employer):
    def __init__(self, name, age):
        super().__init__(name, age)

    def print(self):
        print(f"Рабочий {self.name}, возраст {self.age}")

    def __str__(self):
        return f"Рабочий {self.name}, возраст {self.age}"

    def __int__(self):
        return self.age

m1 = Manager("Петров", 35)
m1.print()
w1 = Worker("Сидоров", 40)
w1.print()
print(w1)
print("Возраст", int(w1))