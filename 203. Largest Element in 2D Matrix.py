def largest_element(matrix):
    largest= float('-inf')
    
    for row in matrix:
        largest = max(largest, max(row))
        
    return largest

matrix=[[1, 4, 8], [2, 7, 4], [1, 8, 10]]

print(largest_element(matrix))