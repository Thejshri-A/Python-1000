def detect_heatwaves(temps, threshold):
    periods=[]
    current_wave=[]
    
    for i, val in enumerate(temps):
        if val>=threshold:
            current_wave.append(i+1)
        else:
            if current_wave:
                periods.append(current_wave)
                current_wave=[]
    if current_wave:
        periods.append(current_wave)
    return periods

temps = [35, 38, 40, 28, 30, 39, 41]
threshold = 35
print(detect_heatwaves(temps, threshold))
        