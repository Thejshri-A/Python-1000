def temperature_peaks(temps):
    return [i for i in range(1, len(temps)-1) if temps[i-1]<temps[i] and temps[i+1]<temps[i]]

temps = [10, 20, 15, 25, 10]
print(temperature_peaks(temps))