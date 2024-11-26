def reverse_words_in_sentence(sentence):
    words=sentence.strip().split()
    reversed_sentence=""
    for word in words[::-1]:
        reversed_sentence+=word
        reversed_sentence+=" "
    
    return reversed_sentence

sentence="This is Amazing"
print(reverse_words_in_sentence(sentence))