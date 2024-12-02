def power_calc(num, power):
    val=1
    if power==0:
        return val
    for i in range(1, power+1):
        val*=num
    return val

print(power_calc(5, 3))