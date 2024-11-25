def min_in_rotated_arr(arr):
    min_val=float('inf')
    
    for i in range(len(arr)):
        if arr[i]<min_val:
            min_val=min(min_val, arr[i])
        else:
            continue
    return min_val
        
arr=[4, 5, 6, 7, 2, 3]
print(min_in_rotated_arr(arr))