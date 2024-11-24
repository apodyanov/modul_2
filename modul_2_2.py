print('Введите 3 (три) целых числа.')
first = input('Введите первое целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
if first == second and second == third:
    print('Среди введённых чисел одинаковых: 3')
elif first == second or first == third or second == third:
    print('Среди введённых чисел одинаковых: 2')
else:
    print('Среди введённых чисел одинаковых: 0')