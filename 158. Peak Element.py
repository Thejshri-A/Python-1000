def find_peak(arr):
    high_val = float("-inf")
    peak_val = float("-inf")
    
    for i in range(1,len(arr)-1):
        if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
            high_val = arr[i]
            peak_val = max(peak_val, high_val)
    return peak_val

arr = [1, 3, 2, 4, 5]
print(find_peak(arr))