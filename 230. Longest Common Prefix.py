def longest_common_prefix(words):
    
    if not words:
        return ""
    
    prefix=words[0]
    
    for s in words[1:]:
        while not s.startswith(prefix):
            prefix=prefix[:-1]
            
            if not prefix:
                return ""
    return prefix

words=["flower", "flow", "flight"]
print(longest_common_prefix(words))