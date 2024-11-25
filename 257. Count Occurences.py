def count_occurences(arr, element):
    
    count=0
    for i in range(len(arr)):
        if arr[i]==element:
            count+=1
        else:
            continue
    return count
arr=[1, 1, 2, 3, 4, 5, 5, 5, 4, 5, 6]
element=5
print(count_occurences(arr, element))