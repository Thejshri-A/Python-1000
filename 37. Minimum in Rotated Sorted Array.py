def min_in_rotated_sorted_array(nums):
    left, right = 0, len(nums)-1
    
    while left<right:
        mid= (left+right)//2
        if nums[right]<nums[mid]:
            left = mid + 1
        else:
            right = mid
    return nums[left]

# Example
nums = [4,5,6,7,0,1,2]
print(min_in_rotated_sorted_array(nums))  # Output: 0
            