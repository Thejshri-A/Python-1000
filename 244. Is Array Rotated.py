def is_arr_rotated(arr1, arr2):
    
    return len(arr1)==len(arr2) and "".join(map(str, arr2)) in "".join(map(str, arr1*2))

arr1=[12, 13, 14, 15]
arr2=[14, 15, 12, 13]
print(is_arr_rotated(arr1, arr2))