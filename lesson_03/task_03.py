# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    return sum(args) - min(args)


print(my_func(8, 6, 9))