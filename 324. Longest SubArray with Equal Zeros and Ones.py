def longest_subarray(arr):
    count=0
    max_len=0
    mapping={0:-1}
    for i, n in enumerate(arr):
        count+=1 if n==1 else -1
        if count in mapping:
            max_len=max(max_len, i-mapping[count])
        else:
            mapping[count]=i
    return max_len
# Example Usage
arr = [0, 1, 0, 1, 1]
print(longest_subarray(arr))  # Output: 4