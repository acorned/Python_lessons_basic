# Задание-1:
# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3

from fractions import Fraction

def fractsum(s):
    fracts = s.split(' + ')
    if len(fracts) == 2:
        sign = 1        
    else:
        fracts = s.split(' - ')
        sign = -1
    fracted = []
    for fract in fracts:
        fractsign = 1
        if fract[0] == '-':
            fract = fract[1:]
            fractsign = -1
        fract = fract.split(' ')
        if len(fract) == 2:
            denominator = int(fract[1].split('/')[1])
            numerator = (int(fract[0]) * denominator + int(fract[1].split('/')[0])) * fractsign         
        else:
            if len(fract[0].split('/')) == 2: 
                denominator = int(fract[0].split('/')[1])
                numerator = (int(fract[0].split('/')[0])) * fractsign
            else:
                denominator = 1
                numerator = int(fract[0]) * fractsign
        fracted.append(Fraction(numerator, denominator))
    result = fracted[0] + sign * fracted[1]
    return '{} {}'.format(result // 1, result % 1)        


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

f = open('./data/workers', encoding = 'utf-8')
db = []
for line in f:
    db.append([word.replace('\n', '') for word in line.split(' ') if word != ''])
g = open('./data/hours_of', encoding = 'utf-8')
for line in g:
    hours = [word.replace('\n', '') for word in line.split(' ') if word != '']
    for man in db:
        if man[0] == hours[0] and man[1] == hours[1]:
            man.append(hours[2])
f.close()
g.close()
db[0].append('Получено')
print('{:<10}{:<10}{:<10}{:<14}{:<13}{:<12}{:<10}'.format(*db[0]))
for man in db[1:]:
    salary, required, done = int(man[2]), int(man[4]), int(man[5])
    if done < required:
        man.append(round(salary * done / required, 2))
    else:
        man.append(round(salary + 2*salary*(done - required)/required, 2))
    print('{:<10}{:<10}{:<10}{:<14}{:<13}{:<12}{:<10}'.format(*man))
    
# Задание-3:
# Дан файл ("data/fruits") со списком фруктов
# Записать в новые файлы все фрукты начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание что нет фруктов начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

