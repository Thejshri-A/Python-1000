def remove_consecutive_duplicates(string):
    result=[]
    for s in string:
        if not result or result[-1]!=s:
            result.append(s)
    return "".join(result)

print(remove_consecutive_duplicates("aabbccaaa"))