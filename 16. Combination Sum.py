def combination_sum(candidates, target):
    result=[]
    
    def backtrack(remaining, start, path):
        if(remaining==0):
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i]>remaining:
                continue
            backtrack( remaining - candidates[i], i, path + [candidates[i]])
            
    backtrack(target, 0, [])
    return result

candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))