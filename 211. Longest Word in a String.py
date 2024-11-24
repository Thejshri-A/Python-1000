def longest_word(sentence):
    words = sentence.strip().split()
    max_word=""
    for word in words:
        if len(word)>len(max_word):
            max_word = word
    return max_word

sentence = "Here is the big sentence to test for a lengthy word"
print(longest_word(sentence))