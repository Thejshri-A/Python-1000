def gcd(num1, num2):
    
    gcd=1
    greater=num2 if num1<num2 else num2
    smaller=num1 if num1<num2 else num2
    
    for i in range(1, smaller+1):
        if num1%i==0 and num2%i==0:
            gcd=i
        
    return gcd

num1=8
num2=32
print(gcd(num1, num2))
        