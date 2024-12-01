def balanced_substring(string):
    balance=0
    count=0
    for s in string:
        balance+=1 if s=="R" else -1
        if balance==0:
            count+=1
    return count

# Example Usage
string = "RLRRLLRLRL"
print(balanced_substring(string))  # Output: 4