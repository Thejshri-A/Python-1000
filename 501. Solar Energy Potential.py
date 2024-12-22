def solar_energy_potential(area , irradiance, efficiency):
    return area*irradiance*efficiency

area = 20
irradiance = 600
efficiency = 0.18
print(solar_energy_potential(area, irradiance, efficiency), "W")