def longest_palindrome_part_in_string(s):
    def expand_around_centre(left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1: right]
    
    longest=""
    for i in range(len(s)):
        odd=expand_around_centre(i, i)
        even=expand_around_centre(i, i+1)
        longest=max(longest, odd, even, key=len)
    return longest

print(longest_palindrome_part_in_string("astoundnuoting"))