def word_count(string):
    
    if not string:
        return 0
    wordCount = 1
    if string[-1]==" ":
        string -= " "
    
    for s in string:
        if s==" ":
            wordCount +=1
        
    return wordCount

string="Hello World! This is a new program. Join us here."
print(word_count(string))