def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i][j-1], grid[i-1][j])
    
    return grid[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(min_path_sum(grid))
         