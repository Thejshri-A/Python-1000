def power_of_two(n):
    return n>0 and (n&(n-1))==0

n=16
print(power_of_two(n))