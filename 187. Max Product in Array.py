def max_prod_in_arr(arr):
    prod = 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                prod = max(prod, arr[i]*arr[j])
    return prod

arr=[1, 16, 2, 4, 3]
print(max_prod_in_arr(arr))