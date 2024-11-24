def transpose_2D_matrix(matrix):
    rows=len(matrix)
    cols = len(matrix[0])
    transposed=[[0]*rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed

matrix=[[1, 2], [3, 4], [5, 6], [7, 8]]
print(transpose_2D_matrix(matrix))