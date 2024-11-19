def numOfIslands(grid):
    if not grid:
        return 0
    
    def dfs(i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
            return
        
        grid[i][j]="0"
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    islands = 0
        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                islands +=1
                dfs(i, j)
    return islands

# Example usage:
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(numOfIslands(grid))  # Output: 3