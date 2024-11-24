import heapq

def second_smallest(arr):
    return heapq.nsmallest(2, arr)[-1]

arr=[1, 3, 3 ,4, 7, 12]
print(second_smallest(arr))