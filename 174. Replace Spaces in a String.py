def replace_spaces_in_string(string):
    new_str = ""
    for char in string:
        if char==" ":
            new_str+="%20"
        else:
            new_str+=char
    return new_str

string="Hello World! This is a new code."
print(replace_spaces_in_string(string))