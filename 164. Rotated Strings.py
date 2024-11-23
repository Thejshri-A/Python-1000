def rotated_strings(string1, string2):
    return len(string1)==len(string2) and string2 in string1+string1

string1="abcdef"
string2="fabcde"
print(rotated_strings(string1, string2))