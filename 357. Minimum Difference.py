def min_difference(arr1, arr2):
    arr1.sort()
    arr2.sort()
    min_diff=float("inf")
    i=j=0
    while i<len(arr1) and j<len(arr2):
        min_diff = min(min_diff, abs(arr1[i]-arr2[j]))
        
        if arr1[i]<arr2[j]:
            i+=1
        else:
            j+=1
    return min_diff

# Example Usage
arr1 = [1, 3, 15, 11, 2]
arr2 = [23, 127, 235, 19, 8]
print(min_difference(arr1, arr2))  # Output: 3