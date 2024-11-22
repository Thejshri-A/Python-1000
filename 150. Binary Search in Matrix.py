def binary_search(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols-1
    
    while row<rows and col>=0:
        if matrix[row][col] == target:
            return True
        
        elif matrix[row][col] > target:
            col -=1
        
        else:
            row +=1
    
    return False

matrix = [[1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16]]
target = 5

print(binary_search(matrix, target))
