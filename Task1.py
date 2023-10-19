"""
Задание 1
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО, дату рождения, контактный телефон, город,
страну, домашний адрес. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к о
тдельным полям через методы класса.
"""

class Human:

    name = 'Vladimir'
    surname = 'Ylianov'
    birthday = 22_04_1870
    phone = 22041870
    city = 'Simbirsk'
    country = 'Russia'
    adress = 'Lenin str'

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAdress(self, adress):
        self.adress = adress

    def getEngine(self):
        return self.adress

    def show(self):
        print(f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"День рождения: {self.birthday}\n"
              f"Телефон: {self.phone}\n"
              f"Город: {self.city}\n"
              f"Страна: {self.country} $\n"
              f"Адрес: {self.adress} $\n")

    def input(self, name, surname, country, birthday, phone, city, adress):
        self.name = name
        self.surname = surname
        self.country = country
        self.birthday = birthday
        self.phone = phone
        self.city = city
        self.adress = adress

    def output(self):
        print(f"Имя: {self.name}\n"
              f"Фамилия: {self.surname}\n"
              f"Страна: {self.country}\n"
              f"День рождения: {self.birthday}\n"
              f"Телефон: {self.phone}\n"
              f"Город: {self.city} руб"
              f"Адрес: {self.adress}\n")


hum = Human()
hum.show()
hum.input('Vladimir', 'Putin', 'Russia', 7_10_1952, 7101952, 'Leningrad', 'Nevsky pr')
hum.output()