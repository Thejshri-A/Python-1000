def number_of_islands(grid):
    def dfs(i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=="0":
            return
        grid[i][j]="0"
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    if not grid:
        return 0
    island_count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="1":
                dfs(i, j)
                island_count+=1
    return island_count

# Example Usage
grid = [
    ['1', '1', '0', '0'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '1']
]
print(number_of_islands(grid))  # Output: 2