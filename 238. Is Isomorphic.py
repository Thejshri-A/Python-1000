def is_isomorphic(s1, s2):
    return len(set(zip(s1, s2)))== len(set(s1)) == len(set(s2))

s1="egg"
s2="add"
print(is_isomorphic(s1, s2))