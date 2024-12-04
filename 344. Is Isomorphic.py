def is_isomorphic(s, t):
    s_mapping, t_mapping = {}, {}
    
    for s_char, t_char in zip(s, t):
        if s_char in s_mapping and s_mapping[s_char] != t_char:
            return False
        if t_char in t_mapping and t_mapping[t_char] != s_char:
            return False
        s_mapping[s_char]=t_char
        t_mapping[t_char]=s_char
    return True

print(is_isomorphic("egg", "add"))