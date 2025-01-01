def energy_consumption_peak(consumption):
    avg_consumption=sum(consumption)/len(consumption)
    threshold=1.2*avg_consumption
    return [val for val in consumption if val>threshold]

consumption = [50, 70, 60, 100]
print(energy_consumption_peak(consumption))