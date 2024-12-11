def extreme_weather_events(temps):
    return [i+1 for i in range(len(temps)) if temps[i]>40 or temps[i]<0]

temps = [-5, 20, 45, 10]
print("Days : ",extreme_weather_events(temps))