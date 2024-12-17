def daily_soil_moisture_level(initial_moisture, rain, evaporation):
    moisture=[initial_moisture]
    for r,e in zip(rain, evaporation):
        moisture.append(moisture[-1]+r-e)
    return moisture[1:]

initial_moisture = 30
rain = [5, 10]
evaporation = [3, 4]
print(daily_soil_moisture_level(initial_moisture, rain, evaporation))       
