my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0  # переменная для задания индекса списка
while n < len(my_list):  # запуск цикла
    num_list = my_list[n]  # задание индекса списка
    n = n + 1 # задание смены индекса списка
    if num_list == 0:
        continue
    elif num_list < 0 or n == len(my_list):
        break
    else:
        print(num_list)