def fibonacci_generation(n):
    fibo = []
    if n==1:
        return [0]
    if n==2 :
        return [0,1]
    else:
        fibo.append(0)
        fibo.append(1)
    
    for i in range(2, n):
        fibo.append(fibo[i-1]+fibo[i-2])
    
    return fibo

n=6
print(fibonacci_generation(n))