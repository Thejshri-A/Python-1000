def reverse_string_recursion(string):
    rev_string=""
    n=len(string)
    
    for i in range(n-1, -1, -1):
        rev_string+=string[i]
    
    return rev_string

string="Hello"
print(reverse_string_recursion(string))