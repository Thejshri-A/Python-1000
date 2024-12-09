def heat_index_calculation(temps, humidities):
    return [round(t+(0.33*h) - 0.7,2) for t,h in zip(temps,humidities)]

temps = [30, 35]
humidities = [70, 60]

print(heat_index_calculation(temps, humidities))