def intersection_of_unsorted(arr1, arr2):
    set1= set(arr1)
    set2 = set(arr2)
    
    return list(set1.intersection(set2))

arr1=[1, 2, 2, 5, 3, 4]
arr2=[2, 3]
print(intersection_of_unsorted(arr1, arr2))