def average_of_arr(arr):
    summing=0
    for i in range(len(arr)):
        summing+=arr[i]
    return int(summing/len(arr))

arr = [1, 2, 3, 4, 5]
print(average_of_arr(arr))