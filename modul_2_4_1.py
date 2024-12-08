n = int(input("Введите целое число в диапазоне от 3 до 20 включительно: "))
result = ''
for i in range(1, n):
    for j in range(2, n):
        if j <= i:
            continue
        if n % (i + j) == 0:
            result += str(i) + str(j)
            print('Для числа:', n, 'Пароль:', result)