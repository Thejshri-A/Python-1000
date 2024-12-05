def majority_element(arr):
    count, candidate = 0, None
    for num in arr:
        if count==0:
            candidate = num
        count+=1 if num==candidate else -1
    return candidate

arr=[3, 2, 3]
print(majority_element(arr))