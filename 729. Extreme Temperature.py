import numpy as np

def extreme_temperature(temps = [30, 35, 40, 45, 50], percentile_temps = 95):
    threshold = np.percentile(temps, percentile_temps)
    extreme=[]
    for temp in temps:
        if temp>threshold:
            extreme.append(temps.index(temp)+1)
    return extreme

print(extreme_temperature())