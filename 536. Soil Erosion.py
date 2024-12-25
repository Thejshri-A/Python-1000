def soil_erosion(initial_soil, rate, years):
    soil=[initial_soil]
    for i in range(years):
        soil.append(soil[-1]*(1-rate))
    return soil

initial_soil = 100
rate = 0.1
years = 3
print(soil_erosion(initial_soil, rate, years))