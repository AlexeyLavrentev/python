# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


list = []

while True:
    n = input('Введите натуральное число: ')
    n = int(n) if n.isdigit() else None
    if n in list:
        list.insert(list.index(n), n)
    else:
        list.append(n)
    print(list)
