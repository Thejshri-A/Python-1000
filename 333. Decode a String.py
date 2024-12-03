def decode(s):
    stack=[]
    curr_string=""
    curr_num = 0
    
    for char in s:
        if char.isdigit():
            curr_num = curr_num*10 + int(char)
        elif char=="[":
            stack.append((curr_string, curr_num))
            curr_string, curr_num = "", 0
        elif char=="]":
            prev_string, num = stack.pop()
            curr_string = prev_string+curr_string*num
        else:
            curr_string+=char
    return curr_string
s = "3[a]2[bc]"
print(decode(s))