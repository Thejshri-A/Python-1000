def urban_heat_island(urban_temps = [40, 42], rural_temps = [35, 38]):
    return [u-r for u,r in zip(urban_temps, rural_temps)]

print(urban_heat_island())