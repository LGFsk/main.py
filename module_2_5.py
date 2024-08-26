def matrix():
    matrix = []
    n = int(input("Введите количество списков: ", ))
    m = int(input("Введите количество элементов списков: ", ))
    value = int(input("Введите значение: ", ))
    for i in range(m):
        matrix.append(value)
    a = matrix[:]
    matrix.clear()
    for i in range(n):
        matrix.append(a)
    print(matrix)
matrix()