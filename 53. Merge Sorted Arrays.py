def mergeSortedArrays(arr1, arr2):
    merged_arr = arr1
    for arr2_val in arr2:
        merged_arr.append(arr2_val)
    merged_arr.sort()
    return merged_arr

arr1 = [1, 4, 7, 9]
arr2 = [2, 3, 5, 7, 11]
print(mergeSortedArrays(arr1, arr2))