def even_count_arr(arr):
    
    count=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count+=1
    return count

arr=[1, 3, 5, 2, 4, 6, 8]
print(even_count_arr(arr))