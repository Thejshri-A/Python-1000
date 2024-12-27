def annual_water_budget(precipitation, evapotranspiration):
    return sum(precipitation)-sum(evapotranspiration)

precipitation = [50, 60, 40]
evapotranspiration = [20, 30, 10]
print(annual_water_budget(precipitation, evapotranspiration))