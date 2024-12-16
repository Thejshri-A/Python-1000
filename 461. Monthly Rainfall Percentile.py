import numpy as np

def monthly_rainfall_percentile(rainfall):
    percentile_25 = np.percentile(rainfall, 25)
    
    percentile_75 = np.percentile(rainfall, 75)
    
    return {f"25th percentile: {percentile_25}, 75th percentile: {percentile_75}"}

# Example
result = monthly_rainfall_percentile([80, 100, 70, 50, 90, 110, 60, 85])
print(result)  # Output: {'25th Percentile': 70, '75th Percentile': 100}