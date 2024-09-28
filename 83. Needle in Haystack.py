def needle_in_haystack(haystack, needle):
    needle_length = len(needle)
    for i in range(len(haystack) - needle_length +1):
        if haystack[i: i + needle_length] == needle:
            return i
    return -1

needle="ell"
haystack="hello"
print(needle_in_haystack(haystack, needle))