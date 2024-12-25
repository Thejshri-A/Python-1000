def temperature_fluctuation(temps):
    max_fluctuation=0
    
    for i in range(len(temps)):
        max_fluctuation=max(max_fluctuation, abs(temps[i]-temps[i-1]))
    return max_fluctuation

temps = [20, 25, 15, 30]
print(temperature_fluctuation(temps))
                            