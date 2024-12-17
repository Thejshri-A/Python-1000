def rainfall_seasonality(rainfall):
    rainfall_avg = sum(rainfall)/len(rainfall)
    wet_months = []
    for i,val in enumerate(rainfall):
        if val>rainfall_avg:
            wet_months.append(i+1)
    return wet_months

rainfall = [50, 60, 90, 70, 40, 30]
print(rainfall_seasonality(rainfall))