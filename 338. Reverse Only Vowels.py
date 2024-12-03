def reverse_only_vowels(s):
    vowels = "aeiouAEIOU"
    left, right = 0, len(s)-1
    s=list(s)
    
    while left<right:
        if s[left] in vowels and s[right] in vowels:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        elif s[left] not in vowels:
            left+=1
        else:
            right-=1
    return "".join(s)

# Example Usage
s = "hello"
print(reverse_only_vowels(s))  # Output: "holle"
