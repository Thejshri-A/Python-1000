def matrix_zero(matrix):
    m, n = len(matrix), len(matrix[0])
    rows_to_zero = set()
    cols_to_zero = set()
    
    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0):
                rows_to_zero.add(i)
                cols_to_zero.add(j)
                
    for i in range(m):
        for j in range(n):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j]=0
                
    return matrix

matrix=[[1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]

print(matrix_zero(matrix))