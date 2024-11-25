def min_difference(arr):
    arr.sort()
    min_diff=float("inf")
    for i in range(1, len(arr)):
        min_diff=min(min_diff, arr[i]-arr[i-1])
    return min_diff
# Example Usage
print(min_difference([4, 9, 1, 32, 13]))