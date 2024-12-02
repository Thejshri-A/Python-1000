import heapq

def k_closest_point(points, k):
    return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)
# Example Usage
points = [[1, 3], [-2, 2], [2, -2]]
k = 2
print(k_closest_point(points, k))  # Output: [[-2, 2], [2, -2]]