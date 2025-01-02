def temperature_change_over_time(temps, time):
    changes=[(temps[i]-temps[i-1])/(time[i]-time[i-1]) for i in range(1, len(temps))]
    avg_rate = sum(changes)/len(changes)
    return f"{avg_rate:.1f}"

temps = [20, 22, 25, 27]
time = [0, 1, 2, 3]
print(temperature_change_over_time(temps, time))