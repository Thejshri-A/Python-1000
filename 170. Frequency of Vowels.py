def frequency_of_vowels(string):
    vowels="aeiou"
    frequency = {v:0 for v in vowels}
    
    for char in string.lower():
        if char in vowels:
            frequency[char]+=1
        
    return frequency

string="hello world"
print(frequency_of_vowels(string))