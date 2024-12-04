def median(arr1, arr2):
    combined=sorted(arr1+arr2)
    n=len(combined)
    if n%2==0:
        return (combined[n//2 - 1]+ combined[n//2])/2
    else:
        return combined[n//2]
    
# Example Usage
arr1 = [1, 3]
arr2 = [2]
print(median(arr1, arr2))  # Output: 2.0