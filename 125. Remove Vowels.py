def removeVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = ""
    
    for s in string:
        if s in vowels:
            continue
        else:
            res +=s
    return res

string="leetcode"
print(removeVowels(string))