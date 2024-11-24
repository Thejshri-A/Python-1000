from collections import defaultdict

def group_anagrams(arr):
    
    groupAnagram = defaultdict(list)
    
    for a in arr:
        sorted_arr = ''.join(sorted(a))
        groupAnagram[sorted_arr].append(a)
        
    return list(groupAnagram.values())

# Example usage
arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(arr))
