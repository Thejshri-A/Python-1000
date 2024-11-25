import bisect

def find_LIS(nums):
    dp=[]
    
    for num in nums:
        pos= bisect.bisect_left(dp, num)
        
        if pos==len(dp):
            dp.append(num)
        else:
            dp[pos]=num
    return dp

nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(find_LIS(nums))