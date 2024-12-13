def missing_positive_number(arr):
    n=len(arr)
    
    for i in range(n):
        while 1<=arr[i]<=n and arr[i]!=arr[arr[i]-1]:
            arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
    
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1

# Example Usage
arr = [7, 8, 9, 11, 12, 1]
print(missing_positive_number(arr))  # Output: 1