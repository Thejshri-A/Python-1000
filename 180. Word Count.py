def word_count(sentence):
    if sentence:    
        count=1
        for char in sentence:
            if char==" ":
                count+=1
        return count
    else:
        return 0
    
sentence="The world is a stage"
print(word_count(sentence))