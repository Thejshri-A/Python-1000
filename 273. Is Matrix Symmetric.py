def is_matrix_symmetric(matrix):
    for i in range(len(matrix)):
        for j in range(0, i):
            if matrix[i][j]!=matrix[j][i]:
                return False
            
    return True

matrix = [ [1, 2, 3], [2, 4, 5], [3, 5, 6] ]
print(is_matrix_symmetric(matrix))
    