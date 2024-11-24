def palindrome_sentence(sentence):
    #Ignore Case and Space
    sentence = sentence.replace(" ","")
    sentence = sentence.lower()
    
    if sentence == "".join(reversed(sentence)):
        return True
    else:
        return False
    
sentence="The Summer isasi remmus eht a"
print(palindrome_sentence(sentence))