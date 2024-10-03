def permute(nums):
    result = []
    
    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
        for i in range(len(remaining)):
            backtrack(path+[remaining[i]], remaining[:i]+remaining[i+1:])
    
    backtrack([], nums)
    return result

# Example
nums = [1, 2, 3]
print(permute(nums))  
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]