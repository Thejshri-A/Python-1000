def soil_moisture_changes(initial_moisture, precipitation , evapotranspiration):
    moisture=[initial_moisture]
    for p,e in zip(precipitation, evapotranspiration):
        moisture.append(moisture[-1]+p-e)
    return moisture

initial_moisture = 100
precipitation = [20, 30]
evapotranspiration = [15, 25]
print(soil_moisture_changes(initial_moisture, precipitation, evapotranspiration))