def longest_prefix_suffix(string):
    n=len(string)
    for length in range(n-1, 0, -1):
        if string[:length]==string[-length:]:
            return string[:length]
    return ""

print(longest_prefix_suffix("abffabf"))