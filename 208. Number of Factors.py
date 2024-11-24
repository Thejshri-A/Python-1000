def number_of_factors(num):
    count=0
    
    for i in range(1, num+1):
        if num%i==0:
            count+=1
    return count

num = 6
print(number_of_factors(num))
        