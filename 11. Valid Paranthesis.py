def is_valid(s):
    stack = []
    valid= {")":"(", "]": "[", "}": "{"}
    
    for char in s:
        if char in valid:
            top_element = stack.pop() if stack else "#"
            if top_element != valid[char]:
                return False
        else:
            stack.append(char)
    return not stack

s="(){[()]}"
print(is_valid(s))