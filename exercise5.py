# 5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга
# . Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

rate_list = [7, 5, 3, 3, 2]

first_val, *middle_chunk, last_val = rate_list
user_el = int(input("Введите элемент рейтинга: "))
last_i = len(rate_list) - 1
counter = 0

if user_el in rate_list:
    new_i = rate_list.index(user_el)
    rate_list.insert(new_i, user_el)
elif user_el > rate_list[0]:
    rate_list.insert(0, user_el)
elif user_el < rate_list[last_i]:
    rate_list.append(user_el)
else:
    while counter < len(middle_chunk):
        next_el = counter + 1
        if middle_chunk[counter] > user_el >= middle_chunk[next_el]:
            rate_list.insert(next_el + 1, user_el)
        counter+=1
print(rate_list)
print(rate_list)

