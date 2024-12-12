def ocean_acidification_events(pH):
    periods=[]
    start=None
    
    for i, val in enumerate(pH):
        if val<7.8:
            if start==None:
                start=i
        else:
            if start is not None:
                periods.append((start, i-1))
                start= None
    if start is not None:
        periods.append((start, len(pH)-1))
    return periods
pH = [8.0, 7.7, 7.6, 7.9, 8.1]
print(ocean_acidification_events(pH))