def count_upper_lower(string):
    lcount=0
    ucount=0
    for s in string:
        if s.islower():
            lcount+=1
        elif s.isupper():
            ucount+=1
    return lcount
print(count_upper_lower("Lets see the Count"))