def prod_except_self(arr):
    prod_arr=[]
    curr_prod=1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                curr_prod *=arr[j]
        prod_arr.append(curr_prod)
        curr_prod=1
    return prod_arr

arr=[1, 2, 3, 4]
print(prod_except_self(arr))