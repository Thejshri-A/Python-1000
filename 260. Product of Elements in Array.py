def prod_in_arr(arr):
    prod=1
    for i in range(len(arr)):
        prod *=arr[i]
    return prod

arr=[1,2, 3, 4, 5, 10]
print(prod_in_arr(arr))