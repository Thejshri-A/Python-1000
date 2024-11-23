from collections import Counter

def first_non_repeating_character_in_string(string):
    count = Counter(string)
    
    for char in string:
        if count[char] == 1:
            return char
        
    
string="leetcodel"
print(first_non_repeating_character_in_string(string))