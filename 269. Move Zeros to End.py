def move_zeros_to_end(arr):
    res=[]
    count_of_zeros=0
    for i in range(len(arr)):
        if arr[i]!=0:
            res.append(arr[i])
        else:
            count_of_zeros+=1
    for i in range(count_of_zeros):
        res.append(0)
        
    return res

arr=[1, 1, 0, 4, 0, 2, 5, 0]
print(move_zeros_to_end(arr))