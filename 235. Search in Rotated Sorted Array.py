def search_rotated(arr, target):
    left, right=0, len(arr)-1
    for i in range(len(arr)):
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        if arr[left]<= arr[mid]:
            if arr[left]<=target<arr[mid]:
                right=mid-1
            else:
                left = mid+1
        else:
            if arr[mid]<target<=arr[right]:
                left=mid+1
            else:
                right=mid-1
    return -1

# Example Usage
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(search_rotated(arr, target))