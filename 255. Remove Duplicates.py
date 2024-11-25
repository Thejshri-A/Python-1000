def remove_duplicates(arr):
    new_arr=[]
    
    for i in range(len(arr)):
        if arr[i] not in new_arr:
            new_arr.append((arr[i]))
        else:
            continue
        
    return new_arr

arr=[1, 1, 2, 3, 5,4 ]
print(remove_duplicates(arr))