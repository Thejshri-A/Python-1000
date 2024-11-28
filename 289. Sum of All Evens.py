def sum_of_evens(arr):
    summation=0
    
    for num in arr:
        if num%2==0:
            summation+=num
    return summation

print(sum_of_evens([1, 2, 3, 4, 5]))