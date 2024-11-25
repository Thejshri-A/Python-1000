def power_set(arr):
    result=[[]]
    
    for num in arr:
        result+=[curr + [num] for curr in result]
        
    return result

arr=[1, 2, 3]
print(power_set(arr))