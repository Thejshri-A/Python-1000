def temp_peak(temps = [32, 35, 29, 40], limit = 34):
    peaks=[]
    for temp in temps:
        if temp>limit:
            peaks.append(temps.index(temp))
    return peaks

print(temp_peak())