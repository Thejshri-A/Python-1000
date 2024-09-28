def inversionCount(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i]>arr[j]:
                inv_count +=1
    return inv_count

# Example
arr = [2, 4, 1, 3, 5]
print(inversionCount(arr))  # Output: 3