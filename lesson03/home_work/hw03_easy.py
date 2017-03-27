# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math

def my_round(number, ndigits):
    if number % 1 != 0:
        ntgrl, frctn = str(number).split('.')  
        if len(frctn) > ndigits:
            if frctn[ndigits] in '01234':
                return float(ntgrl + '.' + frctn[:ndigits])  
            else:
                return float(ntgrl + '.' + str(int(frctn[:ndigits]) + 1))
        else:
            return number
        
my_round(2.1234567, 5)

# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    nums = [int(num) for num in str(ticket_number)]
    return True if sum(nums[:3]) == sum(nums[3:]) else False

