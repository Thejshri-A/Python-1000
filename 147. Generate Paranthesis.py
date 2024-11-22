def generate_paranthesis(n):
    
    def backtrack(s, openCount, closeCount):
        
        if len(s) == 2*n:
            result.append(s)
            return
        
        if openCount<n:
            backtrack(s+"(", openCount+1, closeCount)
        
        if closeCount<openCount:
            backtrack(s+")", openCount, closeCount+1)
        
    result = []
    backtrack("", 0, 0)
    return result

n = 3
print(generate_paranthesis(n))