def soil_moisture_dynamics(initial_moisture = 50, infiltration = [10, 15], evapotranspiration = [5, 8]):
    moisture=[initial_moisture]
    for i,e in zip(infiltration, evapotranspiration):
        moisture.append(moisture[-1]+i-e)
    return moisture[1:]

print(soil_moisture_dynamics())