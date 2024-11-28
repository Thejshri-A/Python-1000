def reverse(string):
    rev=""
    for s in string[::-1]:
        rev+=s
    return rev

string="Hello"
print(reverse(string))