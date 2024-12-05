import heapq

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]

arr=[1, 2, 3, 6, 7, 8]
print(kth_largest(arr, 2))