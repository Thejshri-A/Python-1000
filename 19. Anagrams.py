def group_anagrams(str):
    anagrams={}
    
    for s in str:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
        
    return anagrams

str = ["tea", "ate", "eat", "jut", "tju", "jkl", "lpm", "mlp"]
print(group_anagrams(str))