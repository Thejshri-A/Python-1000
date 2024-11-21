def check_anagrams(str1, str2):
    anagram_1 = {}
    anagram_2 = {}
    
    for s in str1:
        if s not in anagram_1: 
            anagram_1[s] = 1
        else:
            anagram_1[s] += 1
    for s in str2:
        if s not in anagram_2: 
            anagram_2[s] = 1
        else:
            anagram_2[s] += 1
    if anagram_1 == anagram_2:
        return True
    else:
        return False
    
str1 = "silent"
str2 = "listen"
print(check_anagrams(str1, str2))