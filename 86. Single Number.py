def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

nums=[1, 2, 2]
print(singleNumber(nums))