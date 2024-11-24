def equal_array(arr1, arr2):
    #Two Equal array mean they contain two equal elements at same positions
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            if arr1[i]==arr2[i]:
                continue
            else:
                return False
        return True
    return False
    
    
arr1=[1, 2, 3, 4, 5]
arr2=[1, 2, 3, 4, 5]
print(equal_array(arr1, arr2))
            