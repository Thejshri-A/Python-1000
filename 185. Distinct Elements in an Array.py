def distinct_elements(arr):
    distinct_arr = []
    for element in arr:
        if element in distinct_arr:
            continue
        else:
            distinct_arr.append(element)
    return len(distinct_arr)

arr= [1, 2, 3, 3, 4, 5, 5, 6]
print(distinct_elements(arr))