def isPrime(n):
    if n<2:
        return n
    is_prime=[True]*n
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5)+1):
        if is_prime:
            for j in range(i*i, n, i):
                is_prime[j]=False
    return sum(is_prime)

n = 10
print(isPrime(n))