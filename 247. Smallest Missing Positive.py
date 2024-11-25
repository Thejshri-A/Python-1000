def smallest_missing_positive(arr):
    arr=set(arr)
    i=1
    while i in arr:
        i+=1
    return i

arr=[-2, -1, 0, 1, 2, 3, 6, 4]
print(smallest_missing_positive(arr))