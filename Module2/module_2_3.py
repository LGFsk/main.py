my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = len(my_list)
y = 0
while x > 0:
    if my_list[y] > 0:
        print(my_list[y])
        y = y + 1
        x = x - 1
    elif my_list[-x] == 0:
        y = y + 1
        x = x - 1
    elif my_list[-x] < 0:
        break
