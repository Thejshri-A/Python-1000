def sum_of_digits(number):
    num = str(number)
    sum_n = 0
    for n in num:
        sum_n += int(n)
    return sum_n

number=125
print(sum_of_digits(number))