def smallest_missing_positive(arr):
    arr.sort()
    smallest=1
    while smallest in arr:
        smallest+=1
    return smallest

print(smallest_missing_positive([1, 2, 5, 3, 7, 9, 4, 10]))