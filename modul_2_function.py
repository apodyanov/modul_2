def get_matrix(n, m, value):
    matrix = []
    for i in range(n): # данной командой запускается перебор переменной i в диапазоне range(n) (допустим n = 5, след.но
                       # перебор переменной i будет в диапазоне от 5 до 5, то есть задано конкретное число).
        matrix.append([]) # в соотв с усл задачи добавляется пустой список
        for j in range(m): # вот тут происходит волшебство. Пока не могу понять как работает данный механизм.
                           # Георгий может пару слов поясните Спасибо!!!
            matrix[i].append(value) # и тут происходит волшебство... пока так же не могу понять как работает данный механизм.
                                    # Георгий может пару слов поясните Спасибо!!!
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)