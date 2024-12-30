def heat_wave_days(temps, threshold):
    days=[]
    for i, val in enumerate(temps):
        if val>threshold:
            days.append(i+1)
    return days

temps = [35, 42, 30]
threshold = 40
print(heat_wave_days(temps, threshold))