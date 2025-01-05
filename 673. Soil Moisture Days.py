def soil_moisture_days(initial_moisture = 50, rainfall = [10, 5, 0], evaporation = [8, 6, 7]):
    moisture=[initial_moisture]
    for i in range(len(rainfall)):
        moisture.append(moisture[-1]+rainfall[i]-evaporation[i])
    return moisture[1:]

print(soil_moisture_days())