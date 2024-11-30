def second_largest(nums):
    max_val=max(nums)
    sec_max=float("-inf")
    
    for num in nums:
        if num!=max_val:
            sec_max=max(sec_max, num)
            
    return sec_max

nums=[4, 1, 15 ,7, 2, 9, 4, 10]
print(second_largest(nums))