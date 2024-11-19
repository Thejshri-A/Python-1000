from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""
    
    t_count = Counter(t)
    curr_count = {}
    left, right = 0,0
    min_len = float('inf')
    min_window = ""
    formed = 0
    required= len(t_count)
    
    while right<len(s):
        char = s[right]
        curr_count[char] = curr_count.get(char, 0)+1
        if char in t_count and curr_count[char] == t_count[char]:
            formed +=1
        
        while left<=right and formed == required:
            if (right-left+1)<min_len:
                min_len = right-left+1
                min_window = s[left: right+1]
            curr_count[s[left]]-=1
            
            if s[left] in t_count and curr_count[s[left]]<t_count[s[left]]:
                formed -=1
            left +=1
        right+=1
    return min_window


# Example usage:
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"