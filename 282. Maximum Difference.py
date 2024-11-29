def max_diff_in_arr(arr):
    if not arr or len(arr)<2:
        return None
    min_val=arr[0]
    max_diff=0
    
    for num in arr[1:]:
        max_diff=max(max_diff, num-min_val)
        min_val=min(min_val, num)
        
    return max_diff

# Example Usage
arr = [7, 1, 5, 3, 6, 4]
print(max_diff_in_arr(arr))  # Output: 5 (6 - 1)