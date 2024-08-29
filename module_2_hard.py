def input_1():
    field_1 = input("""Введите число от 3 до 20 которое отображается на левом камне: 
    ___________________________________________________
                           """)
    try:
        int(field_1)
        if int(field_1) >= 3 and int(field_1) <= 20:
            return field_1
        else:
            print("Ошибка: не верное число. Повторите ввод")
            print()
            return input_1()
    except:
        try:
            float(field_1)
            print("Ошибка: введено число с запятой. Повторите ввод")
            print()
            return input_1()
        except:
            print("Ошибка: введен текст. Повторите ввод")
            print()
            return input_1()
def rebus():
    rebus = ""
    for i in range(1, 20):
        for j in range(2, 20):
            if i < j:
                if (int(field_1) % int(i + j)) == 0:
                    rebus = str(rebus) + str(i) + str(j)
    print(f"""        Секретный шифр: {rebus}
___________________________________________________""")

stop=1
while stop!="0":
    field_1=input_1()
    rebus()
    stop=input(
    """Хотите прекратить игру "Слишком древний шифр"?
Для остановки введите 0, для продожения любой другой символ:
                                """)


