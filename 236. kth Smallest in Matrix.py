import heapq

def kth_smallest(matrix, k):
    flat_list=[num for row in matrix for num in row]
    
    return heapq.nsmallest(k, flat_list)[-1]

# Example Usage
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 1
print(kth_smallest(matrix, k))