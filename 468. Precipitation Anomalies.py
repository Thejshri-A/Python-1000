def precipitation_anomalies(precipitation):
    average = sum(precipitation)/len(precipitation)
    average_20_above = average+average*0.2
    average_20_below = average-average*0.2
    
    anomalies=[]
    
    for i,val in enumerate(precipitation):
        if val<average_20_below or val>average_20_above:
            anomalies.append(i+1)
    
    return anomalies

precipitation = [80, 120, 90, 70, 110]
print(precipitation_anomalies(precipitation))