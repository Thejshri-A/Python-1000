def factorial_iteration(n):
    if n==1 or n==0:
        return 1
    fact=1
    for i in range(1, n+1):
        fact*=i
    return fact

n=6
print(factorial_iteration(n))