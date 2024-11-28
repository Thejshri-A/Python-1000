def decimal_to_binary(num):
    binary=""
    if num==0:
        return 0
    while num>0:
        binary=str(num%2)+binary
        num=num//2
    return binary

num=11
print(decimal_to_binary(num))