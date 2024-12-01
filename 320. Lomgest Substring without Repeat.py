def longest_substring(s):
    seen={}
    start, max_len=0, 0
    for end, char in enumerate(s):
        if char in seen and seen[char]>=start:
            start=seen[char]+1
        seen[char]= end
        max_len=max(max_len, end-start+1)
    return max_len
# Example Usage
s = "abcabcbb"
print(longest_substring(s))  # Output: 3

    