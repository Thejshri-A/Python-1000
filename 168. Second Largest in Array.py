def second_largest_in_array(arr):
    arr.sort()
    
    return arr[-2] if len(arr)>1 else None

arr= [1, 5, 2, 6, 3, 7, 18, 10]
print(second_largest_in_array(arr))