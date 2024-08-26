def matrix():
    n = int(input("Введите количество списков: ", ))
    m = int(input("Введите количество элементов списков: ", ))
    value = int(input("Введите значение: ", ))
    matrix = []
    for i in range(n):
        matrix.append([] * m)
        for j in range(m):
            matrix[i].append(value)
    print(matrix)


matrix()
