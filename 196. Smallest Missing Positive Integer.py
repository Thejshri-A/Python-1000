def smallest_missing_positive(arr):
    
    max_in_arr = max(arr)
    
    pos_val_in_arr = []
    
    for i in range(len(arr)):
        if arr[i]>=0:
            pos_val_in_arr.append(arr[i])
    min_in_arr = min(pos_val_in_arr)
    print(min_in_arr, max_in_arr)
    for i in range(min_in_arr, max_in_arr):
        if i not in arr:
            return i
        else:
            continue
    
arr=[-1, 0, 1, 3, 4, -100, 2, 7]
print(smallest_missing_positive(arr))
        