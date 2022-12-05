import random

new_List = []
max_index = None
index_counter = range(10)

int_list = (0, 3, 4, 5, 7, 6)
str_list = ('hey', 'well', 'move', 'skip', 'push', 'skr')
bool_list = (True, False, True, False, True, False)
float_list = (2.4, 3.4, 4.6, 0.6, 1.9, 8.5)

for i in index_counter:
    data_type = input('Введите тип данных (int, bool, str, float): ')
    if data_type == 'int':
        max_index = len(int_list) - 1
        new_List.append(int_list[random.randint(0, max_index)])
    elif data_type == 'str':
        max_index = len(str_list) - 1
        new_List.append(str_list[random.randint(0, max_index)])
    elif data_type == 'bool':
        max_index = len(bool_list) - 1
        new_List.append(bool_list[random.randint(0, max_index)])
    elif data_type == 'float':
        max_index = len(float_list) - 1
        new_List.append(float_list[random.randint(0, max_index)])
    else:
        print(f'Error type! {data_type} type does\t exist.')

print(f'Новый список значений - {new_List}')

index0 = 0
index1 = 1
while index0 < len(new_List) - 1:
    (new_List[index0], new_List[index1]) = (new_List[index1], new_List[index0])
    index0+=2
    index1+=2

print(f'Список с замененными значениями - {new_List}')