#   1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
#   Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division_func(a, b):

    try:
        return round(a / b, 3)
    except ZeroDivisionError:
        print('На ноль делить нельзя, введите другое число!')



print(division_func(float(input("Введите делимое: ")), float(input('Введите делитель: '))))