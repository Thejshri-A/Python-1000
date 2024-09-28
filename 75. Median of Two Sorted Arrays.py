def find_median(arr1, arr2):
    arr=sorted(arr1+arr2)
    n=len(arr)
    
    if n%2==1:
        return float(arr[n//2])
    else:
        return (arr[n//2 - 1] + arr[n//2])/2.0
    
# Example
arr1 = [1, 5]
arr2 = [3]
print(find_median(arr1, arr2))  # Output: 2.0