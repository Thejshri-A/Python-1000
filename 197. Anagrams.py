from collections import Counter

def anagrams(str1, str2):
    count = Counter(str1)
    check_anagram = {}
    anagram = True
    for s in str2:
        if s not in check_anagram:
            check_anagram[s]=1
        else:
            check_anagram[s]+=1
    for s in str2:
        if check_anagram[s] == count[s] and len(check_anagram)==len(count):
            anagram=True
        else:
            anagram=False
    return anagram

str1="listen"
str2="silent"
print(anagrams(str1, str2))