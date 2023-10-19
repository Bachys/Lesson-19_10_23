"""
Задание 2
Создайте класс для подсчета максимума из четырех аргументов, минимума из четырех аргументов, средне-арифметического
из четырех аргументов, факториала аргумента. Функциональность необходимо реализовать в виде статических методов.
"""
import math


class Arg:

    @staticmethod
    def Max(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def Min(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def Avg(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def Fact(n):
        if n == 0 or n == 1:
            return 1
        else:
            p = 1
            for i in range(1, n + 1):
                p *= i
            return p


print('Max:', Arg.Max(1, 3, 5, 8))
print('Min:', Arg.Min(2, 6, 9, 33))
print('Среднеарифметическое:', Arg.Avg(2, 5, 8, 7))
print('Factorial:', Arg.Fact(6))
