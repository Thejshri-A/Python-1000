def intersection_arrays(arr1, arr2):
    intersection = []
    arr1_idx, arr2_idx = 0, 0
    
    while arr1_idx<len(arr1) and arr2_idx<len(arr2):
        if arr1[arr1_idx]<arr2[arr2_idx]:
            arr1_idx+=1
        elif arr1[arr1_idx]>arr2[arr2_idx]:
            arr2_idx +=1
        else:
            intersection.append(arr1[arr1_idx])
            arr1_idx+=1
            arr2_idx+=1
    return intersection

arr1=[1, 2, 2, 4, 5]
arr2=[1, 4, 5]
print(intersection_arrays(arr1, arr2))