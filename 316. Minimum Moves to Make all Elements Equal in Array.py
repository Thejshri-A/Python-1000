def min_moves_to_make_equal(arr):
    arr.sort()
    median=arr[len(arr)//2]
    return sum(abs(median-num) for num in arr)

# Example Usage
arr = [1, 2, 3]
print(min_moves_to_make_equal(arr))  # Output: 2