# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 19:47:17 2024

@author: tejashri
"""
def product_except_self(nums):
    if not nums:
        return 0
    output_array = []
    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i !=j:
                prod = prod*nums[j]
        output_array.append(prod)
    return output_array

# Example usage:
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]