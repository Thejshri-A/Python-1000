def kthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(kthLargest(nums, k))  # Output: 5