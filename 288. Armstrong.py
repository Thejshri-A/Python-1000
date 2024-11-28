#Number equals cubes of the digits
def is_armstrong(num):
    val=0
    temp=str(num)
    for i in range(len(str(num))):
        val=val+(int(temp[i])**3)
    if val==num:
        return "Amrstrong"
    else:
        return False
    
num=153
print(is_armstrong(num))