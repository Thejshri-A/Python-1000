def wildfire_risk_days(temps, humids):
    count=0
    for t,h in zip(temps, humids):
        
        if t>35 and h<30:
            count+=1
            
    return count
temps = [30, 36, 40]
humids = [40, 25, 20]
print(wildfire_risk_days(temps, humids))