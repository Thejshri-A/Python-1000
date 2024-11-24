def is_perfect_square(num):
    if num<0:
        return False
    square_root = num**0.5
    if square_root*square_root == num:
        return True
    else:
        return False
    
num=25
print(is_perfect_square(num))