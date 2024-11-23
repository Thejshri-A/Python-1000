import heapq

def kth_largest(arr, k):
    return heapq.nlargest(k, arr)[-1]

arr=[-1, 4, 2, -5, 6, 8]
k=3
print(kth_largest(arr, k))