def kadane_algorithm(arr):
    max_curr = max_global = arr[0]
    
    for num in arr[1:]:
        max_curr=max(num, num+max_curr)
        max_global= max(max_curr, max_global)
    return max_global

# Example Usage
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadane_algorithm(arr))