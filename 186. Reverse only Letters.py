def reverse_only_letters(s):
    letters = [c for c in s if c.isalpha()]
    result = []
    
    for char in s:
        if char.isalpha():
            result.append(letters.pop())
        else:
            result.append(char)
    return "".join(result)

s="abcd-efg-ij-k"
print(reverse_only_letters(s))