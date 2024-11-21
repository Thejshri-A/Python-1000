def palindrome(string):
    length = len(string)
    for i in range(0, length):
        if string[i] == string[length - i - 1]:
            continue
        else:
            return False
    return True

string = "jpalapj"
print(palindrome(string))