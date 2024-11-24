def max_difference_array(arr):
    
    #Larger element comes after the smaller one.
    
    max_diff = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j]>arr[i] and j>i:
                max_diff= max(max_diff, arr[j] - arr[i])
    return max_diff

arr=[7, 1, 5, 3, 6, 4]
print(max_difference_array(arr))