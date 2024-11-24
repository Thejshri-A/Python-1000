from collections import Counter

def first_unique_charac(string):
    
    count= Counter(string)
    
    for s in string:
        if count[s]==1:
            return s

string="lleetcode"
print(first_unique_charac(string))