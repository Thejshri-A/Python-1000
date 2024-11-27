def first_occurence(string, char):
    
    for i in range(len(string)):
        if string[i]==char:
            return i
        
string = "Hello"
char="l"
print(first_occurence(string, char))