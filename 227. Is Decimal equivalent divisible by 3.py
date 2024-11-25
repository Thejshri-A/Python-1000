def dec_div_by_3(binary):
    
    decimal = int(binary, 2)
    
    if decimal%3==0:
        return True
    else:
        return False
binary="110"
print(dec_div_by_3(binary))