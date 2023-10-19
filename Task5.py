"""
Задание 5
Создайте функцию для отображения текущего времени. Произведите декорирование функции. Потенциальный вывод данных на экран:
*********
23:00
*********
В этом выводе на экран две линии из звездочек – результаты декорирования.
"""
import time


class Time:
    def currentTime(fn):
        def wrapeer(self):
            print('***********')
            fn(self)
            print('***********')

        return wrapeer

    @currentTime
    def myTime(self):
        dt = time.gmtime()
        print(dt.tm_hour + 3, ':', dt.tm_min)

dt = Time()
dt.myTime()