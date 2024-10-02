import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


def insert_values(value):
    answer_entry.delete(0, "end")
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = (num1 + num2)
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = (num1 - num2)
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = (num1 * num2)
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = (num1 / num2)
    insert_values(res)


window = tk.Tk()
window.title("Калькулятор Коротков Е.В.")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=3, height=2, command=add)
button_add.place(x=100, y=165)
button_sub = tk.Button(window, text="-", width=3, height=2, command=sub)
button_sub.place(x=140, y=165)
button_mul = tk.Button(window, text="*", width=3, height=2, command=mul)
button_mul.place(x=180, y=165)
button_div = tk.Button(window, text="/", width=3, height=2, command=div)
button_div.place(x=220, y=165)
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=90, y=60)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=90, y=120)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=90, y=255)
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=100, y=30)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=95)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=225)
window.mainloop()
