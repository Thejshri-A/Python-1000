def palindromeNumber(number):
    num = str(number)
    
    length = len(num)
    palindrome = True
    for i in range(length):
        if num[i]==num[length-i-1]:
            palindrome = True
        else:
            return False
    return palindrome

number= 101232101
print(palindromeNumber(number))