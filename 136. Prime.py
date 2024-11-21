def prime(num):
    primeNum = True
    
    for i in range(2, num):
        if num%i==0:
            return False
    return primeNum

num=170
print(prime(num))