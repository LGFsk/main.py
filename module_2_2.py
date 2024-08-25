first = int(input("Введите 1 число: "))
second = int(input("Введите 2 число: "))
third = int(input("Введите 3 число: "))

#Первый вариант
if first == second and second == third:
    print(3)
elif first != second and second != third and first != third:
        print(0)
elif first == second or second == third or first==third:
            print("2")

#второй вариант
if first == second and second == third:
    print(3)
else:
    if first != second and second != third and first != third:
        print(0)
    else:
        if first == second or second == third or first == third:
            print("2")