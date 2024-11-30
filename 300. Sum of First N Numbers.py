def sum_of_n(n):
    summation=0
    for i in range(1, n+1):
        summation+=i
    return summation
print(sum_of_n(10))