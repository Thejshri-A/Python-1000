def subset(nums):
    result = []
    
    def backtrack(start, path):
        result.append(path)
        for i in range(start, len(nums)):
            backtrack(i+1, path+ [nums[i]])
        
    backtrack(0, [])
    return result

nums = [1, 2, 3]
print(subset(nums))