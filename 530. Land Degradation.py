def land_degradation(initial_land, rate, years):
    degradation=[initial_land]
    
    for i in range(years):
        degradation.append(degradation[-1]*(1-rate))
    return degradation

initial_land = 1000
rate = 0.05
years = 4
print(land_degradation(initial_land, rate, years))
    