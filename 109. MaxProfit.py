def maxProfit(nums):
    curr, nex = 0, 0
    for num in nums:
        temp = curr
        curr = max(nex+num, curr)
        nex = temp
    return curr

nums=[2, 7, 9, 3, 1]
print(maxProfit(nums))