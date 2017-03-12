# encoding: utf-8
# Задача-1: Дано произвольное целое число, вывести поочередно цифры исходного числа

def invert(num):
    return [int(let) for let in str(num)]
print(*invert(input('Input number\n')))

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Не нужно решать задачу так: print("a = ", b, "b = ", a) - это неправильное решение!

a, b = input('Input numbers\n').split()
a, b = b, a
print (a, b)

# Задача-3: Запросите у пользователя год рождения. Если ему есть 18 лет, выведите: "Доступ разрешени",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

def access(age):
    return "Access prohibited until 18" if age < 18 else "Access OK"
print(access(2017 - int(input('When did you born?\n'))))
