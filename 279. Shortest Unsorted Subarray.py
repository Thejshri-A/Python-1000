def shortest_unsorted_subarray(arr):
    sorted_arr=sorted(arr)
    left, right=0, len(arr)-1
    
    while left<len(arr) and arr[left]==sorted_arr[left]:
        left+=1
    while right>left and arr[right]==sorted_arr[right]:
        right-=1
    
    return right+left-1 if right>left else 0

print(shortest_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))