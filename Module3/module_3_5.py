def get_multiplied_digits(number):
    str_number = str(number)
    s1_number = str(int(str_number[::-1]))
    str_number= str(int(s1_number[::-1]))
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(24078000)
print(result)
