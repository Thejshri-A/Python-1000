def sum_of_odds(arr):
    
    summing = 0
    for i in range(len(arr)):
        if arr[i]%2!=0:
            summing += arr[i]
    return summing

arr=[1, 2, 3, 4, 5]
print(sum_of_odds(arr))