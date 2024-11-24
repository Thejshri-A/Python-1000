def missing_number(arr):
    n=max(arr)
    
    for i in range(1, n+1):
        if arr[i-1] != i:
            return i
    
    return None

arr=[1, 2, 3, 5, 6, 7, 8]
print(missing_number(arr))