def urban_heat_island(baseline = 30, density = 1000, scaling = 0.002):
    return baseline+density*scaling

print(urban_heat_island())