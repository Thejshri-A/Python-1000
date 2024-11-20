def does_string_contain_only_digits(string):
    valid_int = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for s in string:
        if s in valid_int:
            continue
        else:
            return False
        
    return True

string="123f5"
print(does_string_contain_only_digits(string))