def is_valid(strs):
    mapping={")": "(", "}": "{", "]": "["}
    stack = []
    
    for char in strs:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if top_element != mapping[char]:
                return False
        
        else:
            stack.append(char)
            
    return not stack

# Example
strs = "({}[])"
print(is_valid(strs))  # Output: True