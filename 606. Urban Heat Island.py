def urban_heat_island(temp_urban, temp_rural):
    return [temp_u-temp_r for temp_u, temp_r in zip(temp_urban, temp_rural)]

temp_urban = [35, 36]
temp_rural = [30, 31]
print(urban_heat_island(temp_urban, temp_rural))