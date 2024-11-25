def find_duplicate(arr):
    unique_arr=[]
    duplicates=[]
    
    for i in range(len(arr)):
        if arr[i] not in unique_arr:
            unique_arr.append(arr[i])
        else:
            duplicates.append(arr[i])
    return duplicates

arr=[1, 2, 3, 4, 2,6 ,5 ,3, 5]
print(find_duplicate(arr))