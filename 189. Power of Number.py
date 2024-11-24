def power_of_number(num, power):
    nth_power = 1
    for i in range(1, power+1):
        nth_power *=num
    return nth_power

num=3
power=4
print(power_of_number(num, power))