def urban_heat_island(urban = [35, 36, 37], rural = [30, 31, 32]):
    return [u-r for u,r in zip(urban, rural)]

print(urban_heat_island())