# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib1, fib2 = 0, 1
    for i in range(m + 1):
        if i >= n:
            yield fib1
        fib1, fib2 = fib2, fib1 + fib2
        
print(*fibonacci(8, 15))

# Задача-2:
# Напишите функцию сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную фукцию и метод sort()


def sort_to_max(origin_list):
    if origin_list: return sort_to_max([x for x in origin_list if x < origin_list[0]]) + [x for x in origin_list if x == origin_list[0]] + sort_to_max([x for x in origin_list if x > origin_list[0]])
    return []


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию функции filter
# Разумеется, внутри нельзя использовать саму функцию filter

def own_filter(func, arg):
    return [item for item in arg if func(item) == True]

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма

def isParallel(a1, a2, a3, a4):
    return True if (a1[0] + a2[0] == a3[0] + a4[0] and a1[1] + a2[1] == a3[1] + a4[1]) or (abs(a1[0] - a2[0]) == abs(a3[0] - a4[0]) and abs(a1[1] - a2[1]) == abs(a3[1] - a4[1])) else False

a1, a2, a3, a4 = [2, 4], [-3, 7], [-6, 6], [-1, 3]
print(isParallel(a1, a2, a3, a4))
