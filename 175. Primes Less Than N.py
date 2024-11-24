def prime_less_than_n(n):
    primes_arr=[]
    primes_count=0
    
    for i in range(2, n):
        prime=True
        for j in range(2, int((i**0.5))+1):
            if i%j==0:
                prime = False
                break
            else:
                continue
        if prime==True:
            primes_arr.append(i)
            primes_count+=1
                
    return primes_arr, primes_count

n=15
print(prime_less_than_n(n))