def max_island_area(matrix):
    
    def dfs(i,j):
        if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]==0:
            return 0
        
        matrix[i][j]=0
        return 1+dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
    maxArea=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                maxArea=max(maxArea, dfs(i,j))
    return maxArea

# Example Usage
matrix = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]]
print(max_island_area(matrix))