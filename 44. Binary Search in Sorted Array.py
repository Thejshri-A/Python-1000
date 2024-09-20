def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    for i in range(left, right):
        mid = (left+right)//2
        
        if target == nums[mid]:
            return mid
        
        if target < nums[mid]: #then target lies in left of mid
            right = mid
        else:
            left = mid+1
            
nums=[1, 2, 3, 4, 5]
target = 2
print(binarySearch(nums, target))