def heatwave_severity(temps):
    severity = []
    for temp in temps:
        if 35<=temp<=40:
            severity.append("Moderate")
        elif 40<temp<45:
            severity.append("High")
            
        else:
            severity.append("Please check the value")
    return severity
temps= [34, 36, 42, 41]
print(heatwave_severity(temps))