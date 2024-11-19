# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:47:17 2024

@author: tejashri
"""
def longest_increasing_subArray(nums):
    if not nums:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
            
    return max(dp)

# Example usage:
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_increasing_subArray(nums))  # Output: 4