# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    print(f'Сумма двух наибольших аргументов равна: {a + b + c - min([a, b, c])}')


my_func(int(input('Введите первое целое число:')),
        int(input('Введите первое целое число:')),
        int(input('Введите первое целое число:')),)