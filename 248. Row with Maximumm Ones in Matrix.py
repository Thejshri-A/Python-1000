def row_with_max_ones(matrix):
    row_max_count=-1
    row_max_idx=-1
    
    for i, row in enumerate(matrix):
        count = row.count(1)
        if count>row_max_count:
            row_max_count=max(row_max_count, count)
            row_max_idx=i
        
    return row_max_idx
# Example Usage
matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0]
]
print(row_with_max_ones(matrix))