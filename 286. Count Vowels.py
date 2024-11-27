def count_vowels(string):
    vowels = "aeiouAEIOU"
    count=0
    for s in string:
        if s in vowels:
            count+=1
    return count

print(count_vowels("Hello"))