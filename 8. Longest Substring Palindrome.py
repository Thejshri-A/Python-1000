
#Palindrome

def longest_palindrome(s):
    def expand_around_center(left, right):
        while left>=0 and right <len(s) and s[left]==s[right]:
            left -=1
            right +=1
        return s[left+1: right]
    if len(s)<2:
        return s
    result=""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(i, i)
        even_palindrome = expand_around_center(i, i+1)
        result=max(result, odd_palindrome, even_palindrome, key=len)
    return result

s="ebflolfrsrflol"
print(longest_palindrome(s))