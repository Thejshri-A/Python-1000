def findPeak(nums):
    left, right = 0, len(nums)-1
    while left<right:
        mid = (left+right)//2
        if nums[mid]<nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return left

# Example
nums = [1, 2, 3, 1]
print(findPeak(nums))  # Output: 2 (index of 3)
    