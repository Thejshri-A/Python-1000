from collections import Counter

def is_unique_all(string):
    count=Counter(string)
    
    for s in string:
        if count[s]==1:
            continue
        else:
            return False
        
    return True

string="abcdefe"
print(is_unique_all(string))
    