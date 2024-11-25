def find_peak(arr):
    for i in range(len(arr)):
        if (i==0 or arr[i]>arr[i-1]) and (i==len(arr)-1 or arr[i]>arr[i+1]):
            return i
        
# Example Usage
print(find_peak([1, 2, 3, 1]))