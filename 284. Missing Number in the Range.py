def missing_number_in_range(arr):
    min_val=min(arr)
    max_val=max(arr)
    
    for i in range(min_val, max_val):
        if i not in arr:
            return i
        
    return None

arr=[4, 5, 7, 8, 9]
print(missing_number_in_range(arr))
        