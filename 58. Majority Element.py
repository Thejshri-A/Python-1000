def majority_element(nums):
    count, candidate = 0, None
    for num in nums:
        if count == 0:
            candidate = num
        else:
            candidate+= (1 if candidate == num else -1)
        
    return candidate

# Example
nums = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(nums)) #Output = 2