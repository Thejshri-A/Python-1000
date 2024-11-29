def triplet_to_zero(nums):
    nums.sort()
    result=set()
    
    for i, num in enumerate(nums):
        target=-num
        seen=set()
        for j in range(i+1, len(nums)):
            complement=target-nums[j]
            if complement in seen:
                result.add((num, nums[j], complement))
            seen.add(nums[j])
    return [list(triplet) for triplet in result]

# Example Usage
print(triplet_to_zero([-1, 0, 1, 2, -1, -4]))