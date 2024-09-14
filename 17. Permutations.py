def permute(nums):
    result= []
    
    def backtrack(start=0):
        if start==len(nums):
            result.append(nums[:])
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start+1)
            nums[start], nums[i] = nums[i], nums[start]
            
    backtrack()
    return result

nums = [1, 2, 3]
print(permute(nums))
    
    