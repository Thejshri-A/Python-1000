def intersection_of_two_arr(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1=[1, 2, 3, 4, 5, 6]
arr2=[2, 4, 6, 8]
print(intersection_of_two_arr(arr1, arr2))