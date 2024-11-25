def count_ones(n):
    count=0
    while n:
        count+= n&1
        n>>=1
    return count

n=11
print(count_ones(n))