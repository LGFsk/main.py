def matrix():

    matrix = []
    for i in range(n):
        matrix.append([] * n)
        for j in range(m):
            matrix[i].append(value)
    print(matrix)

n = int(input("Введите количество списков: ", ))
m = int(input("Введите количество элементов списков: ", ))
value = int(input("Введите значение: ", ))
matrix()
