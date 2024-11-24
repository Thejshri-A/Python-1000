def is_list_sorted(arr):
    check_arr=sorted(arr)
    
    for i in range(len(arr)):
        if arr[i]==check_arr[i]:
            continue
        else:
            return "Not Sorted"
        
    return "Sorted"

arr= [1, 3, 5, 17, 40]
print(is_list_sorted(arr))