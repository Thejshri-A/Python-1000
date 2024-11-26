def second_largest(arr):
    max_val=max(arr)
    sec_arr= arr
    sec_arr.remove(max_val)
    sec_max_val=max(sec_arr)
    return sec_max_val

arr=[1, 2, 3, 4, 7, 5, 6]
print(second_largest(arr))