from collections import Counter
def reorganize(s):
    count=Counter(s)
    
    sorted_chars = sorted(count.items(), key=lambda x: -x[1])
    
    result=[]
    
    while len(result)<len(s):
        for i, (char, freq) in enumerate(sorted_chars):
            if freq>0:
                if not result or result[-1]!=char:
                    result.append(char)
                    sorted_chars[i]=(char, freq-1)
                    break
        else:
            return ""
        
    return "".join(result)

# Example Usage
s = "aaabb"
print(reorganize(s))  # Output: "ababa"
    