def sum_of_squares(arr):
    summation=0
    for num in arr:
        summation+=num*num
    return summation

arr=[1, 2, 3]
print(sum_of_squares(arr))