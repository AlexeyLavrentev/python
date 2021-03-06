# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб).
#                                        Физика:   30(л)   —   10(лаб)
#                                        Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open('file4.txt', 'r', encoding='utf-8') as f:
    items_dict = {}
    for line in f.readlines():
        items = line.rstrip().split()
        quantity = 0
        for item in items[1:]:
            quantity += int(''.join(filter(lambda x: x.isdigit(), item)))
            quantity += int(''.join(n for n in item if n.isdigit()))
        items_dict.update({items[0]: quantity})
print(items_dict)