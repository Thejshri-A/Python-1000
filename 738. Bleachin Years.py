def bleaching_years(anomalies = [0.8, 1.2, 0.9, 1.5]):
    years=[]
    for val in anomalies:
        if val>1:
            years.append(anomalies.index(val))
    return years

print(bleaching_years())