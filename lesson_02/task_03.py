# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.


month = input('Введите месяц в виде целого числа от 1 до 12: ')
month = int(month) if month.isdigit() else 0

# решение через list:
list = ['зима', 'весна', 'лето', 'осень']

if (0 < month < 3) or month == 12:
    print(list[0])
elif 2 < month < 6:
    print(list[1])
elif 5 < month < 9:
    print(list[2])
elif 8 < month < 12:
    print(list[3])
else:
    print('Введены некорректные данные')

    # решение через dict:
dict = {'зима': {12, 1, 2}, 'весна': set(range(3, 6)), 'лето': set(range(6, 9)), 'осень': set(range(9, 12))}

for key, value in dict.items():
    if month in value:
        print(key)