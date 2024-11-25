def single_using_XOR(arr):
    
    result=0
    
    for a in arr:
        result^=a
    return result

arr=[1, 2, 1, 3, 2, 4]
print(single_using_XOR(arr))