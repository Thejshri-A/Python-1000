def is_unique_all(str1, str2):
    sorted_str1=sorted(str1)
    sorted_str2= sorted(str2)
    
    return sorted_str1==sorted_str2

str1="talk"
str2="lakt"
print(is_unique_all(str1, str2))
    