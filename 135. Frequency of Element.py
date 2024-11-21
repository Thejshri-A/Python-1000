def frequency(arr):
    freq = {}
    
    for n in arr:
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] +=1
        
    return freq

arr = [1, 1, 1, 1, 1, 2, 3, 4, 4, 5, 6, 7, 1]
print(frequency(arr))