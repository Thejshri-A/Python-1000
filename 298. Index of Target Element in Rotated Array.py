def index_of_element(arr, target):
    left, right=0, len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if arr[left]<arr[mid]:
            if arr[left]<=target<arr[right]:
                right=mid-1
            else:
                left=mid+1
        else:
            if arr[mid]<target<=arr[right]:
                left=mid+1
            else:
                right=mid-1
    return -1
                
arr=[4, 5, 6, 1, 2, 3]
target=6
print(index_of_element(arr, target))