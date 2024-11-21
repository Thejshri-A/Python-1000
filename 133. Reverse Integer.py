def reverse_an_integer(number):
    num = str(number)
    res = ""
    for i in range(len(num)-1, -1, -1):
        res += num[i]
        
    return int(res)

number = 1234435
print(reverse_an_integer(number))
        