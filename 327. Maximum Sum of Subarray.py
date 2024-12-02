def maximum_subarray_sum(nums):
    max_curr= max_global = 0
    for num in nums:
        max_curr = max(num, max_curr+num)
        max_global = max(max_curr, max_global)
    return max_global

# Example Usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray_sum(nums))  # Output: 6