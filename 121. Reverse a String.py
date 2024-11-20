def reverseString(string):
    res = ""
    for i in range(len(string)-1, -1, -1):
        res += string[i]
        
    return res

string = "hello"
print(reverseString(string))