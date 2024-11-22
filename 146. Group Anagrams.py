from collections import defaultdict

def groupAnagrams(atring):
    
    anagram_group = defaultdict(list)
    
    for word in string:
        key = ''.join(sorted(word))
        anagram_group[key].append(word)
        
    return list(anagram_group.values())

string = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(string))