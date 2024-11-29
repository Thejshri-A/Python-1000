def reverse_digits_of_number(num):
    str_num=str(num)
    rev_str_num=""
    for s in str_num[::-1]:
        rev_str_num+=s
    rev_num=int(rev_str_num)
    return rev_num
print(reverse_digits_of_number(1234))