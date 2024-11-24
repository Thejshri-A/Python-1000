def armstrong_num(num):
    str_num = str(num)
    len_num = len(str_num)
    
    total = sum(int(digit)**len_num for digit in str_num)
    
    return total==num

num=155
print(armstrong_num(num))