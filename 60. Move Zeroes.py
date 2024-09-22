def move_zeroes(nums):
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at +=1
    return nums

nums = [1, 2, 0, 4, 5, 0 ,6, 7]
print(move_zeroes(nums))