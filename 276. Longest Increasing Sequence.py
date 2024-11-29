import bisect
def lis(nums):
    dp=[]
    for num in nums:
        idx=bisect.bisect_left(dp, num)
        if idx==len(dp):
            dp.append(num)
        else:
            dp[idx]=num
    return dp

# Example Usage
print(lis([10, 9, 2, 5, 3, 7, 101, 18]))