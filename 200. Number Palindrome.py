def number_palindrome(num):
    rev_num=0
    org_num=num
    while num%10>0:
        temp = num%10
        rev_num = rev_num*10 + temp
        num = num//10
    if rev_num == org_num:
        return True
    else:
        return False
    
num=1234321
print(number_palindrome(num))
        