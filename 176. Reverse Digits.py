def reverse_digits(num):
    res=0
    while num%10 >0:
        temp= num%10
        res= res*10+temp
        num=num//10
    return res

num=1234
print(reverse_digits(num))
    