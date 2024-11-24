def remove_space_from_string(sentence):
    sentence= sentence.replace(" ", "")
    return sentence

sentence = "This is a new program to remove the spaces inbetween."
print(remove_space_from_string(sentence))