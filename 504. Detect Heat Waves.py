def detect_heat_waves(temperatures, threshold):
    heat_waves=[]
    for i,temp in enumerate(temperatures):
        if temp>threshold:
            heat_waves.append(i+1)
    return heat_waves

temperatures = [34, 40, 37]
threshold = 35
print(detect_heat_waves(temperatures, threshold))