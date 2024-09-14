def can_jump(nums):
    furthest = 0
    for i in range(len(nums)):
        if i > furthest:
            return False
        furthest = max(furthest, i + nums[i])
        print(furthest)
        
    return True

nums = [1, 3, 0, 0, 4]
print(can_jump(nums))