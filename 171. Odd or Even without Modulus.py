def odd_even_without_modulus(num):
    half = int(num/2)
    temp = 0
    for i in range(half):
        temp +=2
    if temp==num:
        return "Even"
    else:
        return "Odd"
    
num = 461
print(odd_even_without_modulus(num))