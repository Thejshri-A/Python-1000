def rainfall_trend(rainfall):
    if all(rainfall[i]<rainfall[i+1] for i in range(len(rainfall)-1)):
        return "Increasing"
    elif all(rainfall[i]>rainfall[i+1] for i in range(len(rainfall)-1)):
        return "Decreasing"
    else:
        return "Stable"
    
print(rainfall_trend([150, 130, 110]))