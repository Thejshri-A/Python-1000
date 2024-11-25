def string_rotation_check(str1, str2):
    combined_str= str1+str2
    
    if len(str1)==len(str2) and str2 in combined_str:
        return True
    else:
        return False
    
str1="abcdef"
str2="cdefab"

print(string_rotation_check(str1, str2))
        