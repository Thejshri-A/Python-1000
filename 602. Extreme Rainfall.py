import numpy as np

def extreme_rainfall(rainfall, percentile=75):
    threshold=np.percentile(rainfall, percentile)
    extremes=[i+1 for i,rain in enumerate(rainfall) if rain>threshold]
    
    return extremes

rainfall = [10, 15, 30, 5, 25]
percentile = 95
print(extreme_rainfall(rainfall, percentile))