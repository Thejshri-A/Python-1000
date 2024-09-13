def roman_to_int(s):
    roman_int_map = { "I": 1, "V": 5,
                     "X": 10, "L": 50,
                     "C": 100, "D" : 500,
                     "M": 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        value = roman_int_map[char]
        
        if value<prev_value:
            total -= value
        else:
            total += value
            
        prev_value = value
        
    return total

s="MCCXLI"

print(roman_to_int(s))