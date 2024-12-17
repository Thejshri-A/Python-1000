def global_temperature_anomalies(temps):
    
    return ["Positive" if temp>0 else "Negative" for temp in temps]

temps = [-0.2, 0.3, -0.1, 0.5]
print(global_temperature_anomalies(temps))
    