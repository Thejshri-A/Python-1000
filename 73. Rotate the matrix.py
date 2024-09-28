def rotate_matrix(matrix):
    n = len(matrix)
    
    #Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    #Reverse the rows in the matrix
    for i in range(n):
        matrix[i].reverse()
    return matrix

# Example
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(rotate_matrix(matrix))
  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]