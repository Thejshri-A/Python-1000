def heatwave_days(temps):
    count=0
    for temp in temps:
        if temp>35:
            count+=1
    return count

temps = [34, 36, 37, 33, 38, 32]
print(heatwave_days(temps))