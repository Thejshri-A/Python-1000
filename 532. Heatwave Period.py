def heatwave_period(temps, threshold):
    periods=[]
    start=None
    for i, val in enumerate(temps):
        if val>threshold:
            if start is None:
                start=i+1
        else:
            if start is not None:
                periods.append((start,i))
                start=None
    if start is not None:
        periods.append((start,len(temps)))
    return periods
            
    
temps = [35, 37, 33, 40, 42]
threshold = 36
print(heatwave_period(temps, threshold))