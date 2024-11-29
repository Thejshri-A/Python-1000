from collections import Counter

def is_equal_frequency(string):
    count=Counter(string)
    return len(set(count.values()))==1

string="aabbccdd"
print(is_equal_frequency(string))
        