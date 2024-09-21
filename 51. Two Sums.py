def twoSums(nums, target):
    rem=0
    for i in range(len(nums)):
        rem=target-nums[i]
        for j in range(len(nums)):
            if rem==nums[j]:
                return i, j

nums=[1, 2, 3,4]
target=6
print(twoSums(nums, target))