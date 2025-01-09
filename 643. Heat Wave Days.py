def heat_wave_days(temperatures = [34, 40, 45, 30], threshold = 42):
    heat=[]
    for val in temperatures:
        if val>threshold:
            heat.append(temperatures.index(val))
    return heat

print(heat_wave_days())