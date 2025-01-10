def detect_heatwave(temperatures = [32, 35, 36, 31, 30], threshold = 34):
    heatwave=[]
    for temp in temperatures:
        if temp>threshold:
            heatwave.append(temperatures.index(temp)+1)
    return heatwave

print(detect_heatwave())