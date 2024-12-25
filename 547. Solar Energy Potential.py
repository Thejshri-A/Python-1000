def solar_energy_potential(area, radiation, hours):
    return area*radiation*hours

area = 50
radiation = 5
hours = 6
print(solar_energy_potential(area, radiation, hours), "kWh")