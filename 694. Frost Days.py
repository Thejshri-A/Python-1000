def frost_days(temperatures = [3, -2, 5, -1, 0]):
    frosts=[]
    for temp in temperatures:
        if temp<0:
            frosts.append(temperatures.index(temp)+1)
    return frosts


print(frost_days())