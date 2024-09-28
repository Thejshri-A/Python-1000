from collections import Counter

def uni_char(string):
    count = Counter(string)
    
    for i, char in enumerate(string):
        if count[char] == 1:
            return i
    return -1

string="loveleetcode"
print(uni_char(string))
    