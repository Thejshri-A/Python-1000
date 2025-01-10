def urban_heat_island(urban_temp = [35, 36, 34], rural_temp = [30, 31, 29]):
    return [u-r for u,r in zip(urban_temp, rural_temp)]

print(urban_heat_island())