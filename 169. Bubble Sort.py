def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums=[1, 4, 3, 2, 5, 4, 5]
print(bubble_sort(nums))