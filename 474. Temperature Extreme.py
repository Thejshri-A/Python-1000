def temperature_extreme(temps):
    max_temp=max(temps)
    min_temp= min(temps)
    
    return f"Maximum Temperature at {max_temp}, Minimum Temperature at {min_temp}"
temps=[15, 20, 35, 10, 25]
print(temperature_extreme(temps))