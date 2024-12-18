# РЕКУРСИЯ
#from inspect import stack

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n - 1)
#
# print(summa(5))

# stack = []
# stack.append(1)
# print('Добавили элемент', stack)
# stack.append(2)
# print('Добавили элемент', stack)
# stack.append(3)
# print('Добавили элемент', stack)
# print(stack)
# print()
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# stack.pop()
# print('Убрали элемент', stack)
# print(stack)
# Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    #n = 0
    if len(str_number) > 1: #and str_number.endswith(str(n)):
        #list(str_number).pop() здесь пытаюсь избавиться от возможного нуля в конце числа, так как в задаче оба ответа = 24, но не получается...
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
# консоль 24

result2 = get_multiplied_digits(402030)
print(result2)
# консоль 0

