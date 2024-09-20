def kthLargestNumber(nums, k):
    nums.sort()
    
        
    return nums[-k]

nums=[1, 2, 3, 4, 5]
k=4
print(kthLargestNumber(nums, k))