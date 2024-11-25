def is_matrix_toeplitz(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j]!=matrix[i+1][j+1]:
                return False
    return True

# Example Usage
matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [6, 5, 1, 2]
]
print(is_matrix_toeplitz(matrix))