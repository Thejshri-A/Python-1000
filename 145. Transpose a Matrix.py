def transposeMatrix(matrix):
    return [[matrix[row][col] for row in range(len(matrix))] for col in range(len(matrix[0]))]

# Example usage:
matrix = [[1, 2, 3], [4, 5, 6]]
result = transposeMatrix(matrix)
print(result)  # Output: [[1, 4], [2, 5], [3, 6]]