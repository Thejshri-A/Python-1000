def longest_substring_without_repeat(string):
    char_set = {}
    left = 0
    max_len = 0
    
    for i in range(len(string)):
        if string[i] in char_set:
            left = max(left, char_set[string[i]]+1)
        char_set[string[i]]=i
        max_len= max(max_len, i-left+1)
        
    return max_len

s = "abcabcbb"
print(longest_substring_without_repeat(s))  # Output: 3
