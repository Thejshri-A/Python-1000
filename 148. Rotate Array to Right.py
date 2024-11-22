def rotate_array_to_right(arr, k):
    #Rotating to the Right
    res = []
    rotate = len(arr)-k
    
    for i in range(rotate, len(arr)):
        res.append(arr[i])
    for i in range(0, rotate):
        res.append(arr[i])
    return res

arr=[1, 2, 3, 4, 5, 6, 7]
k=4
print(rotate_array_to_right(arr, k))