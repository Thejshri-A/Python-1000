def arr_rot(arr1, arr2):
    combined=arr1+arr2
    return len(arr1)==len(arr2) and arr1 == combined[:len(arr2)]

arr1=[1, 2, 3, 4]
arr2=[3, 4, 1, 2]

print(arr_rot(arr1, arr2))