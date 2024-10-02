def draw_area():
    for i in area:
        print(*i)
    print()

def check_winner():
    if area[0][0] == "X" and area[0][1] == "X" and area[0][2] == "X":
        return "X"
    return "*"


area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
print("Добро пожаловать в крестики-нолики")
print("__________________________________")
draw_area()
for turn in range(1, 10):
    print(f'Ход {turn}')
    if turn % 2 == 0:
        turn_char = "0"
        print("Ходят Нолики")
    else:
        turn_char = "X"
        print("Ходят Крестики")
    row = int(input("Введите номер строки (1,2,3): ")) - 1
    column = int(input("Введите номер столбца (1,2,3): ")) - 1
    if area[row][column] == "*":
        area[row][column] = turn_char
    else:
        print("Ячейка занята, вы пропускаете ход")
        draw_area()
        continue

    draw_area()

    print(check_winner())

    if check_winner() == "X":
        print("Крестики победили")
        break
    elif check_winner() == "0":
        print("Нолики победили")
        break
    elif check_winner() == "*" and turn == 9:
        print("Ничья")

