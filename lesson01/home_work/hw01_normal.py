# encoding: utf-8                                         
# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа

def max_digit(num):
    return max([int(let) for let in str(num)])

print(max_digit(input('Input number\n')))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу используя только две переменные

a, b = input('Input numbers\n').split()
a, b = b, a
print (a, b)

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида ax2 + bx + c = 0.
# Для вычисления квадратного корня воспользуйтесь функицй sqrt() молудя math
from math import sqrt
def squareroots(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return 'No real roots'
    else:
        return 'Roots: %d, %d' % ((-b + sqrt(d))/ (2 * a), (-b - sqrt(d))/ (2 * a))

a, b, c = [int(s) for s in input('Input a, b and c\n').split()]
print (squareroots(a, b, c))
