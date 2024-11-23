def sum_in_diagonal(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))

matrix=[[1, 2, 3], [4, 15, 6], [7, 8, 9]]
print(sum_in_diagonal(matrix))