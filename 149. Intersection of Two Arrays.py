#Given two arrays, return their intersection as an array of unique elements.
def intersection_of_arrays(arr1, arr2):
    
    res = []
    
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] in arr2:
                if arr1[i] not in res:
                    res.append(arr1[i])
    
    return res

arr1 = [1, 2, 5, 6, 124, 2, 1]
arr2 = [2, 2, 124, 1]
print(intersection_of_arrays(arr1, arr2))