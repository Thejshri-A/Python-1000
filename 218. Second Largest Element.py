import heapq

def second_largest(arr, k):
    return heapq.nlargest(k, arr)[1]

# Example Usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(second_largest(nums, k))