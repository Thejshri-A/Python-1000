from collections import Counter

def first_unique_character(string):
    count=Counter(string)
    
    for s in string:
        if count[s]==1:
            return s
        
string="swiss"
print(first_unique_character(string))