def remove_vowels(string):
    vowels= ["a", "e", "i", "o", "u"]
    new_string=""
    
    for s in string:
        if s in vowels:
            continue
        else:
            new_string+=s
    return new_string

string="The vast ocean!"
print(remove_vowels(string))