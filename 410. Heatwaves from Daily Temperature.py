"""
Given daily maximum temperatures, identify heatwave periods 
where temperatures exceed 35°C for 3 or more consecutive days.
Example:
Input: temps = [34, 36, 37, 38, 33, 35, 36, 37, 30]
Output: Heatwave periods: [(1, 3), (5, 7)]



"""

def heatwaves_from_daily_temperature(temps, threshold):
    heatwave_periods = []
    start=None
    
    for i, temp in enumerate(temps):
        if temp>threshold:
            if start is None:
                start=i
                
        else:
            if start is not None and (i-start)>=3:
                heatwave_periods.append((start, i-1))
                start=None
    if start is not None and (len(temps)-start) >=3:
        heatwave_periods.append((start, len(temps)-1))
    return heatwave_periods

temps = [34, 36, 37, 38, 33, 35, 36, 37, 30]
threshold=35
print(heatwaves_from_daily_temperature(temps, threshold))
        