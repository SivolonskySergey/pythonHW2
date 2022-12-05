import random

new_list = []

list_of_values = [12,'sfdsf', 763, 0.34, True, False, 349, 378,
                889.09, 4629, 2, 'fhdke r r', 'true', 534.09]

list_length = (len(list_of_values)) - 1
lengthOfNewList = range(8)

for i in lengthOfNewList:
    new_list.append(list_of_values[random.randint(0, list_length)])
    
print(f'Заполненный массив - {new_list}')

for el in new_list:
    print(f'{el} - is {type(el)}')









