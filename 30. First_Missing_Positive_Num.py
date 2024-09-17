def first_missing_positive_number(nums):
    n = len(nums)
    for i in range(n):
        while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
            nums[nums[i]-1], nums[i]= nums[i], nums[nums[i]-1]
    for i in range(n):
        if nums[i]!= i + 1:
            return i+1
    return n+1

nums=[-1, 1, 3, 4]
print(first_missing_positive_number(nums))