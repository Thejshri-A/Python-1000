def sum_of_digits(num):
    res = 0
    while num>0:
        res += num%10
        num = num//10
    return res

num=1234
print(sum_of_digits(num))
        