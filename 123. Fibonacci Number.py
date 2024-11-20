def FibonacciNumber(n):
    zeroth, first = 0,1
    fibbo_arr = [zeroth, first]
    if n==0:
        return 0
    elif n==1:
        return 1
    curr, nex = zeroth, first
    for i in range(2, n+1):
        fibbo_arr.append(curr+nex)
        curr= nex
        nex=fibbo_arr[i]
    return fibbo_arr[n]

n=2
print(FibonacciNumber(n))