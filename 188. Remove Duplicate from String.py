def remove_duplicate(string):
    
    new_string = ""
    
    for c in string:
        if c not in new_string:
            new_string+=c
        else:
            continue
    return new_string

string="programming"
print(remove_duplicate(string))