def findingMissingNumber(arr):
    max_in_arr = max(arr)
    min_in_arr = min(arr)
    
    for i in range(min_in_arr, max_in_arr+1):
        if i not in arr:
            return i
        
    return False

arr = [3, 0, 1, 2, 4, 5, 8, 6, 7, 10]
print(findingMissingNumber(arr))