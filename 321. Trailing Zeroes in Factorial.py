def trailing_zeroes_in_factorial(number):
    count=0
    while number>0:
        number//=5
        count+=number
    return count

print(trailing_zeroes_in_factorial(500))