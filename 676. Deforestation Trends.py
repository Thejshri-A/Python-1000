def deforestation_trend(areas = [1000, 950, 920]):
    trend=[]
    for i in range(1, len(areas)):
        val=((areas[i-1]-areas[i])/areas[i-1])*100
        trend.append(val)
    return trend

print(deforestation_trend())