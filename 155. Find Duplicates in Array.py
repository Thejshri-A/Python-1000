def duplicate_in_array(arr):
    no_dup = []
    find_dup = []
    
    for i in range(len(arr)):
        if arr[i] not in no_dup:
            no_dup.append(arr[i])
        elif arr[i] not in find_dup:
            find_dup.append(arr[i])
        
    return find_dup

arr = [1, 2, 3, 4,7 ,4, 3, 9,2 ,3 ,5 ,6]
print(duplicate_in_array(arr))            