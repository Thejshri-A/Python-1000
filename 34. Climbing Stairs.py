def climbing_stairs(num):
    if num<=2:
        return num
    
    a, b = 1, 2
    for i in range(3, num+1):
        a, b = b, a+b
    
    return b

n = 5
print(climbing_stairs(n))
        