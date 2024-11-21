def smallest_number_in_array(arr):
    small = float('inf')
    
    for i in range(len(arr)):
        if arr[i]<small:
            small = arr[i]
        
    return small

arr = [1, 2, 3, 4, 5, ]
print(smallest_number_in_array(arr))