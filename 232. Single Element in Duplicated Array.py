from collections import Counter

def single_element_in_duplicated_arr(arr):
    count=Counter(arr)
    single_element=[]
    
    for i in range(len(arr)):
        if count[arr[i]]==1:
            single_element.append(arr[i])
    return single_element

arr=[1, 2, 1, 2, 4, 5, 4, 6]
print(single_element_in_duplicated_arr(arr))