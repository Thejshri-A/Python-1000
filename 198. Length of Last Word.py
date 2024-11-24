def len_of_last_word(sentence):
    words= sentence.strip().split()
    return len(words[-1]) if words else None

sentence = "This is a Hello Sentence"
print(len_of_last_word(sentence))