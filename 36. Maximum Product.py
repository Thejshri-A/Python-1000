def max_product(nums):
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(nums[i], max_prod*nums[i])
        min_prod = min(nums[i], min_prod*nums[i])
        result = max(result, max_prod)
        
    return result

# Example
nums = [2,3,-2,4]
print(max_product(nums))  # Output: 6