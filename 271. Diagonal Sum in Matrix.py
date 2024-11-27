def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(diagonal_sum(matrix))