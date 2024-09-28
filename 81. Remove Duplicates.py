def removeDup(arr):
    uni_arr = []
    arr.sort()
    for i in range(0, len(arr)):
        if arr[i-1]==arr[i]:
            continue
        else:
            uni_arr.append(arr[i])
            
    return uni_arr

arr = [1, 1, 1, 4, 5, 6, 6]
print(removeDup(arr))
