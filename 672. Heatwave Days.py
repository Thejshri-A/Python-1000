def heatwave_days(temperatures = [35, 42, 40, 43, 30, 32], threshold = 40):
    heat=[]
    for i,temp in enumerate(temperatures):
        if temp>=threshold:
            heat.append(i+1)
    return heat

print(heatwave_days())