def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

a, b = 2, 8
print(gcd(a, b))