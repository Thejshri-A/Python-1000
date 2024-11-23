def reverse_string(string):
    res = ""
    for word in string.split(" ")[::-1]:
        res += word
        res += " "
    return res

string="Sky is Vast and Blue"
print(reverse_string(string))