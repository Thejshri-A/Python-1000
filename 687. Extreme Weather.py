def extreme_weather(temps = [38, 42], precip = [50, 120]):
    extremes=[]
    for i in range(len(temps)):
        if temps[i]>40 or precip[i]>100:
            extremes.append(i+1)
    return extremes

print(extreme_weather())