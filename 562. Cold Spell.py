def cold_spell(temps, threshold):
    
    periods=[]
    start=None
    for i, val in enumerate(temps):
        if val<threshold:
            if start is None:
                start=i+1
        else:
            if start is not None:
                periods.append([start, i])
                start=None
    if start is not None:
        periods.append([start, len(temps)])
    
    return periods

temps = [10, 12, 5, 6, 14]
threshold = 10
print(cold_spell(temps, threshold))