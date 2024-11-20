def max_in_arr(arr):
    
    max_val = float('-inf')
    
    for val in arr:
        max_val = max(val, max_val)
        
    return max_val

arr = [1, 4, 3, 2, 6, 1, 7, 8, 12, 14, 15, 90]
print(max_in_arr(arr))