def temperature_inversion(temps_high, temps_low):
    inversion=[i+1 for i in range(len(temps_high)) if temps_high[i]>temps_low[i]]
    return inversion

temps_low = [15, 18, 10]
temps_high = [10, 20, 12]
print(temperature_inversion(temps_high, temps_low))