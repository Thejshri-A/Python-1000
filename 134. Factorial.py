def factorial_calculation(n):
    factorial = 1
    
    for i in range(1, n+1):
        factorial *= i
    
    return factorial

n=8
print(factorial_calculation(n))