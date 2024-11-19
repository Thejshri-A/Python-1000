def combinationSums(candidates, target):
    result = []
    
    def backtrack(remaining,path, start):
        if remaining == 0:
            result.append(path)
            return
        elif remaining<0:
            return
        for i in range(start, len(candidates)):
            backtrack(remaining-candidates[i], path+[candidates[i]], i)
        
        
    backtrack(target, [], 0)
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSums(candidates, target))  # Output: [[2, 2, 3], [7]]