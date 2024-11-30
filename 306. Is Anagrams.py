from collections import Counter

def is_anagrams(str1, str2):
    count1=Counter(str1)
    count2=Counter(str2)
    
    for s in str2:
        if count1[s]==count2[s]:
            continue
        else:
            return False
    return True

str1, str2 = "this", "histt"
print(is_anagrams(str1, str2))