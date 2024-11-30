def smallest_missing_positive_integer(nums):
    nums=set(nums)
    smallest=1
    while smallest in nums:
        smallest+=1
    return smallest

nums=[1, 4, 2, 6, -4, -7, 4]
print(smallest_missing_positive_integer(nums))