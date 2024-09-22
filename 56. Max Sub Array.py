def maxSubArray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums:
        curr_sum = max(num, num+curr_sum)
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums)) #Output = 6