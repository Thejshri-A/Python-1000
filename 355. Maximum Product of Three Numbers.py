def maximum_prod_of_three(arr):
    return max(arr[-1]*arr[-2]*arr[-3], arr[0]*arr[1]*arr[-1])

arr=[-10, -10, 5, 2]
print(maximum_prod_of_three(arr))