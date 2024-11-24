def first_repeat_in_string(string):
    new_string=""
    
    for s in string:
        if s in new_string:
            return s
        else:
            new_string+=s
    return "No Repeating Character in the String"

string="abcebkk"
print(first_repeat_in_string(string))