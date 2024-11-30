def maximum_product_of_two_number_in_arr(arr):
    arr.sort()
    return max(arr[0]*arr[1], arr[-1]*arr[-2])

arr=[1, 3, 2, 4, -5, -4]
print(maximum_product_of_two_number_in_arr(arr))