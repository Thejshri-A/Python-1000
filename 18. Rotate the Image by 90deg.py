def rotate(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    for rows in matrix:
        rows.reverse()
        
    return matrix

matrix = [ [1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]
    ]

print("Original Matrix : ", matrix)

rotate(matrix)
print(" After Rotating : ", matrix)