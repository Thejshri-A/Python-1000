def sortColors(nums):
    low, mid, high = 0, 0, len(nums)-1
    
    while mid<=high:
        if nums[mid]==0: #Mid is the current index being checked, if it is zero, swap with low
            nums[low], nums[mid] = nums[mid], nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1: #if mid value in nums is 1, just increment index by 1 as this is middle part of flag
            mid+=1
        else: #if mid value in nums is 2, then swap with high , as it is high part of flag
            nums[high], nums[mid] = nums[mid], nums[high]
            high -=1
    return nums

nums = [1, 0, 1, 1, 0, 2, 2, 1, 2]
print(sortColors(nums))