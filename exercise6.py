# data_list = []
# while True:
#     data_list.append(('Номер элемента: ', {
#         'Название': input('Название элемента: '),
#         'Цена': input('Цена элемента: '),
#         'Количество': input('Количество элементов: '),
#         'ед.': input('Единица измерения: ')
#     }))
#     stop = input('Завершить ввод? да/нет: ')
#     if stop == 'да':
#         break

names_list = []
prices_list = []
amount_list = []
items_list = []
stat_list = {}

stat_data = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'ед': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'ед': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'ед': 'шт.'})
]

for i in range(len(stat_data)):
    names_list.append(stat_data[i][1]['название'])
    prices_list.append(stat_data[i][1]['цена'])
    amount_list.append(stat_data[i][1]['количество'])
    items_list.append(stat_data[i][1]['ед'])

stat_list.update({'Названия': names_list, 'Цены': prices_list,
                  'Количество': amount_list, 'единицы': list(set(items_list))})
print(stat_list)