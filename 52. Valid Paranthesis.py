def validParanthesis(s):
    stack_str=[]
    dict_str={")":"(", "]":"[", "}": "{"}
    
    for i in s:
        if i in dict_str:
            top_element= stack_str.pop() if stack_str else"#"
            if dict_str[i] != top_element:
                return False
        else:
            stack_str.append(i)
    return not stack_str

# Example Output
s = "()[]{}"
print(validParanthesis(s))  # Output: True

