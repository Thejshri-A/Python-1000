def remove_duplicate(nums):
    
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.pop(i+1)
        else:
            i+=1
    return nums

nums = [1, 1, 23, 56, 56, 89, 100]
print(remove_duplicate(nums))