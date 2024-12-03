def product_except_self(arr):
    prod=1
    new_arr=[]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                prod*=arr[j]
        new_arr.append(prod)
        prod=1
    return new_arr

arr=[1, 2, 3, 4]
print(product_except_self(arr))